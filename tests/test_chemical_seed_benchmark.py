"""Finite reconstruction and leakage checks for the chemistry benchmark."""

import csv
import hashlib
import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "07_emergence_laboratory" / "chemistry"
SPEC = importlib.util.spec_from_file_location("bond_energy_benchmark",
                                            LAB / "reproduce_bond_energy.py")
benchmark = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(benchmark)


class ChemicalSeedBenchmarkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = benchmark.load_dataset()
        cls.results = benchmark.reproduce(cls.rows)

    def test_source_bytes_and_finite_factorization(self):
        hashes = {
            "bond_energy_dataset.csv":
                "d866c96c14178402c3a8a974f09977d2facc43f0e45abceab22d3642961e4244",
            "supplied_model_results.csv":
                "25c29054a1c9a0ddb61c9dff77807fe87cfdbdf4af96dad7fc474762cfbf9656",
            "supplied_feature_ranking.csv":
                "ee03aa8f95b0c4c8dbb29a86107f697d9cd088b0b985760277985dbc68ddfe55",
        }
        for name, digest in hashes.items():
            self.assertEqual(hashlib.sha256((LAB / "data" / name).read_bytes()).hexdigest(),
                             digest)
        self.assertEqual(len(self.rows), 47)
        self.assertEqual(len(self.results["elements"]), 10)
        self.assertEqual(self.results["identity"]["groups"], [14, 15, 16, 17])
        self.assertEqual(self.results["identity"]["max_absolute_error"], 0)
        feature = benchmark.feature_matrix
        np.testing.assert_allclose(feature(self.rows, ("rV_sum",)),
                                   2 * feature(self.rows, ("group_reciprocal_10",)),
                                   atol=1e-15, rtol=0)
        np.testing.assert_allclose(
            self.results["models"]["rV_sum"]["bond_predictions_kJ_mol"],
            self.results["models"]["group_reciprocal_10"]["bond_predictions_kJ_mol"],
            atol=1e-11, rtol=0,
        )

    def test_supplied_predictions_and_all_eight_feature_metrics(self):
        models = self.results["models"]
        with (LAB / "data" / "supplied_feature_ranking.csv").open(newline="") as stream:
            ranking = list(csv.DictReader(stream))
        self.assertEqual(len(ranking), 8)
        for row in ranking:
            for metric in ("rmse_kJ_mol", "mae_kJ_mol", "r2"):
                self.assertAlmostEqual(models[row["feature"]]["by_bond"][metric],
                                       float(row[metric]), places=9)
        supplied_names = {
            "baseline_no_second_coordinate": "baseline",
            "ROSI_seed": "rV_sum",
            "no_seed_generic_symbolic_search": "group_reciprocal_13",
            "no_seed_exact_rV_equivalent": "group_reciprocal_10",
        }
        with (LAB / "data" / "supplied_model_results.csv").open(newline="") as stream:
            for row in csv.DictReader(stream):
                if row["condition"] not in supplied_names:
                    # This summary-only permutation result is not reconstructible.
                    self.assertEqual(row["condition"], "fake_seed_null_median_best_of_8")
                    continue
                name = supplied_names[row["condition"]]
                for metric in ("rmse_kJ_mol", "mae_kJ_mol", "r2"):
                    self.assertAlmostEqual(models[name]["by_bond"][metric],
                                           float(row[metric]), places=9)
        self.assertAlmostEqual(models["baseline"]["by_prediction"]["rmse_kJ_mol"],
                               55.049743026775566, places=9)
        self.assertAlmostEqual(models["rV_sum"]["by_prediction"]["rmse_kJ_mol"],
                               52.080882697172356, places=9)

    def test_fold_audit_excludes_element_and_uses_training_statistics(self):
        details = self.results["models"]["rV_sum"]
        matrix = benchmark.feature_matrix(self.rows, ("en_diff", "rV_sum"))
        for fold in details["folds"]:
            element = fold["held_out_element"]
            train, test = fold["train_indices"], fold["test_indices"]
            self.assertFalse(set(train) & set(test))
            self.assertEqual(set(train) | set(test), set(range(47)))
            for index in train:
                self.assertNotIn(element, (self.rows[index]["A"], self.rows[index]["B"]))
            for index in test:
                self.assertIn(element, (self.rows[index]["A"], self.rows[index]["B"]))
            np.testing.assert_allclose(fold["feature_mean"], matrix[train].mean(axis=0))
            np.testing.assert_allclose(fold["feature_scale"], matrix[train].std(axis=0))
        self.assertEqual(len(details["events"]), 85)
        self.assertEqual(details["prediction_counts"],
                         [1 if row["A"] == row["B"] else 2 for row in self.rows])
        # Alter only the C-fold test observations, including their targets.
        changed = [dict(row) for row in self.rows]
        for row in changed:
            if "C" in (row["A"], row["B"]):
                row["en_diff"] += 100
                row["rV_sum"] *= 10
                row["bond_energy_kJ_mol"] += 10000
        new = benchmark.leave_one_element_out(changed, ("en_diff", "rV_sum"))
        original_c = next(f for f in details["folds"] if f["held_out_element"] == "C")
        changed_c = next(f for f in new["folds"] if f["held_out_element"] == "C")
        self.assertEqual(original_c, changed_c)

    def test_duplicate_pair_and_invalid_model_inputs_are_rejected(self):
        constant_target = benchmark.score_predictions([1, 1], [1, 1])
        self.assertIsNone(constant_target["r2"])
        self.assertEqual(constant_target["rmse_kJ_mol"], 0)
        text = (LAB / "data" / "bond_energy_dataset.csv").read_text(encoding="utf-8")
        lines = text.splitlines()
        duplicate = lines[1].split(",")
        duplicate[0], duplicate[1] = duplicate[1], duplicate[0]
        with patch.object(Path, "open", return_value=io.StringIO(
                text + ",".join(duplicate) + "\n")):
            with self.assertRaisesRegex(ValueError, "duplicate unordered bond"):
                benchmark.load_dataset()
        for alpha in (0, -1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                benchmark.leave_one_element_out(self.rows, ("en_diff",), alpha=alpha)
        pole_rows = [dict(row) for row in self.rows]
        pole_rows[0]["group_A"] = 13
        with self.assertRaisesRegex(ValueError, "pole"):
            benchmark.feature_matrix(pole_rows, ("group_reciprocal_13",))


if __name__ == "__main__":
    unittest.main()
