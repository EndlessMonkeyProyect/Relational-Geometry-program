"""Cheap controls for the growth laboratory, not the 80 full source trajectories."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "07_emergence_laboratory/growth/scripts/transient_bias_growth.py"
spec = importlib.util.spec_from_file_location("transient_bias_growth", MODULE)
growth = importlib.util.module_from_spec(spec)
spec.loader.exec_module(growth)


class SeedBiasGrowthTests(unittest.TestCase):
    def test_geometry_and_symmetry(self):
        square = {(x, y) for x in range(-1, 2) for y in range(-1, 2)}
        result = growth.shape_metrics(square)
        self.assertEqual(result["aspect"], 1)
        self.assertEqual(result["compactness"], 1)
        self.assertEqual(result["perimeter"], 12)
        self.assertAlmostEqual(result["m2"], 0)
        line = {(0, 0), (1, 0), (2, 0)}
        self.assertAlmostEqual(growth.shape_metrics(line)["m2"], 1)
        self.assertAlmostEqual(growth.shape_metrics({(y, x) for x, y in line})["m2"], -1)
        self.assertEqual(growth.shape_metrics({(4, 5)})["perimeter"], 4)
        with self.assertRaises(ValueError):
            growth.shape_metrics(set())

    def test_deterministic_ordered_growth_and_connectivity(self):
        args = dict(n_sites=80, seed=104, strength=3, decay_tau=20, cutoff=25)
        first = growth.grow(**args)
        self.assertEqual(first, growth.grow(**args))
        occupied, trace, final = first
        self.assertEqual(len(occupied), 80)
        self.assertEqual(trace[-1], {"n": 80, **final})
        reached, pending = {(0, 0)}, [(0, 0)]
        while pending:
            x, y = pending.pop()
            for dx, dy in growth.NEIGH8:
                point = (x + dx, y + dy)
                if point in occupied and point not in reached:
                    reached.add(point)
                    pending.append(point)
        self.assertEqual(reached, occupied)

    def test_exact_cutoff_and_parameter_validation(self):
        self.assertGreater(growth.bias_amplitude(9, 6, 300, 10), 0)
        self.assertEqual(growth.bias_amplitude(10, 6, 300, 10), 0)
        self.assertEqual(growth.bias_amplitude(11, 6, 300, 10), 0)
        # With the field disabled from the first addition both streams coincide.
        self.assertEqual(growth.grow(60, strength=6, cutoff=1),
                         growth.grow(60, strength=0, cutoff=1))
        for kwargs in ({"n_sites": 0}, {"decay_tau": 0}, {"beta": -1},
                       {"strength": float("nan")}, {"cutoff": 0}, {"cutoff": 1.5},
                       {"checkpoints": (401,)}):
            with self.assertRaises(ValueError):
                growth.grow(**kwargs)

    def test_paired_bootstrap_resamples_pairs(self):
        a = np.array([0., 10., 100., 1000.])
        result = growth.paired_bootstrap(a, a + 2, reps=100)
        self.assertEqual(result["difference_mean"], 2)
        self.assertEqual(result["ci95_low"], 2)
        self.assertEqual(result["ci95_high"], 2)
        self.assertEqual(result, growth.paired_bootstrap(a, a + 2, reps=100))
        with self.assertRaises(ValueError):
            growth.paired_bootstrap([1], [2])
        with self.assertRaises(ValueError):
            growth.paired_bootstrap([1, 2], [2])

    def test_signed_mean_is_not_mean_absolute_or_rms(self):
        rows = [{"condition": "transient_bias", "n": 10, "m2": a, "q4": .1}
                for a in (-.5, .5)]
        summary = growth.trace_summary(rows)[0]
        self.assertEqual(summary["m2_signed_mean"], 0)
        self.assertEqual(summary["m2_mean_absolute"], .5)
        self.assertEqual(summary["m2_rms"], .5)

    def test_source_bytes_pairing_and_means(self):
        expected = {
            "supplied_growth_trace.csv": "2f090ce8f9828f64af922eee69b9db661053c8c15f1dc8dd8baaeaa4f3202edb",
            "supplied_final_runs.csv": "81b17b0eb7540529c0a834f1aa0001f0ed773914b1a5d6329091c22811f912d2",
            "supplied_unpaired_comparison.csv": "da42f19afdf917e836ea6876258f950f68388bcd53f9ddabf24baac5868fb20b",
        }
        for filename, digest in expected.items():
            self.assertEqual(hashlib.sha256((growth.DATA_DIR / filename).read_bytes()).hexdigest(), digest)
        summary = growth.reanalyze_supplied(reps=100)["summary"]
        self.assertEqual(summary["source_rows"], {"final": 80, "trace": 560, "pairs": 40})
        self.assertFalse(summary["microstates_available"])
        q4 = next(row for row in summary["comparison"] if row["metric"] == "q4")
        self.assertAlmostEqual(q4["no_bias_mean"], .13878740897589076)
        self.assertAlmostEqual(q4["transient_bias_mean"], .13907566899461576)
        finals = [{"condition": "no_bias", "run": 0, **dict.fromkeys(growth.METRICS, 1.)},
                  {"condition": "transient_bias", "run": 1, **dict.fromkeys(growth.METRICS, 1.)}]
        with self.assertRaises(ValueError):
            growth.compare_pairs(finals)

    def test_small_experiment_microstates_and_explicit_export(self):
        result = growth.experiment(n_runs=2, n_sites=35, strength=0, reps=20)
        self.assertEqual(result["summary"]["exact_equal_pairs"], 2)
        self.assertEqual(result["summary"]["microstate_jaccard_mean"], 1.)
        self.assertEqual(len(result["final_rows"]), 4)
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "result"
            growth.write_outputs(result, target)
            saved = json.loads((target / "summary.json").read_text(encoding="utf-8"))
            self.assertEqual(saved["protocol"], growth.PROTOCOL)
            microstates = json.loads((target / "microstates.json").read_text(encoding="utf-8"))
            self.assertEqual(len(microstates["no_bias"][0]), 35)
            with self.assertRaises(FileExistsError):
                growth.write_outputs(result, target)

    def test_cli_without_output_dir_writes_no_outputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            command = [sys.executable, "-B", str(MODULE), "--n-runs", "2",
                       "--n-sites", "20", "--bootstrap-reps", "20"]
            process = subprocess.run(command, cwd=temporary, text=True, capture_output=True)
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertEqual(json.loads(process.stdout)["config"]["n_sites"], 20)
            self.assertEqual(list(Path(temporary).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
