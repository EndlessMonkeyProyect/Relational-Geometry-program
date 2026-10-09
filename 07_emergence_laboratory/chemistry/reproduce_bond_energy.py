"""Reconstruct fixed chemical-descriptor comparisons with NumPy only.

This is a new, transparent reconstruction of the supplied report's predictions,
not the missing original search/permutation program. It does not perform feature
selection, search, bootstrap, or permutations and never writes output files.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np


DATA_DIR = Path(__file__).resolve().parent / "data"
DEFAULT_DATASET = DATA_DIR / "bond_energy_dataset.csv"
SEED_FEATURES = (
    "rV_sum", "rV_prod", "both_prime_weight", "rV_diff",
    "P_sum", "P_prod", "P_diff", "same_P",
)
MODEL_FEATURES = {
    "baseline": ("en_diff",),
    **{name: ("en_diff", name) for name in SEED_FEATURES},
    "group_reciprocal_10": ("en_diff", "group_reciprocal_10"),
    "group_reciprocal_13": ("en_diff", "group_reciprocal_13"),
}
REQUIRED_COLUMNS = {
    "A", "B", "bond_energy_kJ_mol", "en_diff",
    "group_A", "group_B", "rV_A", "rV_B", *SEED_FEATURES,
}


def load_dataset(path=DEFAULT_DATASET):
    """Read without modifying source values; reject missing/duplicate records."""
    with Path(path).open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = reader.fieldnames or []
        if len(fields) != len(set(fields)) or not REQUIRED_COLUMNS <= set(fields):
            raise ValueError("Missing required columns or duplicate CSV headers")
        rows = []
        pairs = set()
        for raw in reader:
            if None in raw or any(value is None for value in raw.values()):
                raise ValueError("Malformed CSV row")
            a, b = raw["A"].strip(), raw["B"].strip()
            pair = tuple(sorted((a, b)))
            if not a or not b or pair in pairs:
                raise ValueError("Empty element label or duplicate unordered bond")
            pairs.add(pair)
            numeric = {key: float(value) for key, value in raw.items()
                       if key not in ("A", "B")}
            if not all(np.isfinite(value) for value in numeric.values()):
                raise ValueError("Non-finite or missing numeric observation")
            rows.append({"A": a, "B": b, **numeric})
    if not rows:
        raise ValueError("Empty dataset")
    return rows


def feature_matrix(rows, names):
    """Evaluate fixed formulas; no fitted transform is calculated here."""
    columns = []
    for name in names:
        if name in ("group_reciprocal_10", "group_reciprocal_13"):
            shift = int(name.rsplit("_", 1)[1])
            groups = np.array([[row["group_A"], row["group_B"]]
                               for row in rows], dtype=float)
            if np.any(groups == shift):
                raise ValueError("Reciprocal feature is undefined at its pole")
            column = np.sum(1.0 / (groups - shift), axis=1)
        else:
            column = np.array([row[name] for row in rows], dtype=float)
        columns.append(column)
    matrix = np.column_stack(columns)
    if not np.all(np.isfinite(matrix)):
        raise ValueError("Non-finite feature")
    return matrix


def score_predictions(target, prediction):
    """RMSE and MAE have target units; R2 is undefined for constant targets."""
    target, prediction = np.asarray(target), np.asarray(prediction)
    residual = target - prediction
    squared_error = float(np.sum(residual**2))
    denominator = float(np.sum((target - np.mean(target))**2))
    return {
        "rmse_kJ_mol": float(np.sqrt(np.mean(residual**2))),
        "mae_kJ_mol": float(np.mean(np.abs(residual))),
        "r2": 1.0 - squared_error / denominator if denominator > 0 else None,
    }


def leave_one_element_out(rows, names, alpha=1.0):
    """Fit scaler and Ridge within each fold and expose its training metadata.

    Every bond containing the held-out element is absent from that fold's
    training data. A heteronuclear bond receives two out-of-fold predictions;
    a homonuclear bond receives one. Both scoring conventions are returned.
    Ridge minimizes ||y - intercept - Z beta||^2 + alpha ||beta||^2, with
    population-standardized training features Z and an unpenalized intercept.
    """
    if not np.isfinite(alpha) or alpha <= 0:
        raise ValueError("alpha must be finite and positive")
    matrix = feature_matrix(rows, names)
    target = np.array([row["bond_energy_kJ_mol"] for row in rows], dtype=float)
    elements = sorted({row[side] for row in rows for side in ("A", "B")})
    sums = np.zeros(len(rows), dtype=float)
    counts = np.zeros(len(rows), dtype=int)
    events = []
    folds = []
    for element in elements:
        test_mask = np.array([element in (row["A"], row["B"]) for row in rows])
        train_indices = np.flatnonzero(~test_mask)
        test_indices = np.flatnonzero(test_mask)
        if not train_indices.size or not test_indices.size:
            raise ValueError("Each element fold needs training and test observations")
        training = matrix[train_indices]
        mean = np.mean(training, axis=0)
        scale = np.std(training, axis=0, ddof=0)
        scale = np.where(scale == 0, 1.0, scale)
        z_train = (training - mean) / scale
        target_mean = float(np.mean(target[train_indices]))
        coefficient = np.linalg.solve(
            z_train.T @ z_train + alpha * np.eye(len(names)),
            z_train.T @ (target[train_indices] - target_mean),
        )
        prediction = (matrix[test_indices] - mean) / scale @ coefficient + target_mean
        sums[test_indices] += prediction
        counts[test_indices] += 1
        folds.append({
            "held_out_element": element,
            "train_indices": train_indices.tolist(),
            "test_indices": test_indices.tolist(),
            "feature_mean": mean.tolist(),
            "feature_scale": scale.tolist(),
            "target_mean": target_mean,
            "coefficient": coefficient.tolist(),
        })
        events.extend({
            "row_index": int(index),
            "held_out_element": element,
            "prediction_kJ_mol": float(predicted),
        } for index, predicted in zip(test_indices, prediction))
    if np.any(counts == 0):
        raise ValueError("An observation received no out-of-fold prediction")
    bond_predictions = sums / counts
    event_targets = np.array([target[event["row_index"]] for event in events])
    event_predictions = np.array([event["prediction_kJ_mol"] for event in events])
    return {
        "features": list(names),
        "alpha": float(alpha),
        "by_bond": score_predictions(target, bond_predictions),
        "by_prediction": score_predictions(event_targets, event_predictions),
        "prediction_counts": counts.tolist(),
        "bond_predictions_kJ_mol": bond_predictions.tolist(),
        "events": events,
        "folds": folds,
    }


def identity_check(rows):
    """Check rV = 2/(group-10) on the supplied finite domain only."""
    groups = np.array([row[f"group_{side}"] for row in rows for side in ("A", "B")])
    rv = np.array([row[f"rV_{side}"] for row in rows for side in ("A", "B")])
    if np.any(groups == 10):
        raise ValueError("rV identity is undefined at group 10")
    errors = np.abs(rv - 2.0 / (groups - 10))
    return {
        "groups": sorted(set(groups.tolist())),
        "max_absolute_error": float(np.max(errors)),
        "identity_holds_at_1e_15": bool(np.all(errors <= 1e-15)),
    }


def reproduce(rows):
    return {
        "rows": len(rows),
        "elements": sorted({row[side] for row in rows for side in ("A", "B")}),
        "identity": identity_check(rows),
        "models": {name: leave_one_element_out(rows, features)
                   for name, features in MODEL_FEATURES.items()},
        "scope": (
            "Fixed-model reconstruction only. Formula selection, search history, "
            "500 permutations and reported bootstrap are not reproduced."
        ),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--json", action="store_true",
                        help="Print full results including fold audit metadata")
    args = parser.parse_args(argv)
    result = reproduce(load_dataset(args.dataset))
    if args.json:
        print(json.dumps(result, indent=2, allow_nan=False))
        return
    print(f"Observations: {result['rows']}; elements: {len(result['elements'])}")
    print("Ridge alpha=1; scaler fitted within each leave-one-element-out fold.")
    print("RMSE (kJ/mol): by_bond averages predictions first; by_prediction concatenates.")
    for name, details in result["models"].items():
        bond, event = details["by_bond"], details["by_prediction"]
        r2_display = f"{bond['r2']:.9f}" if bond["r2"] is not None else "undefined"
        print(f"{name:24} by_bond={bond['rmse_kJ_mol']:.9f}  "
              f"by_prediction={event['rmse_kJ_mol']:.9f}  "
              f"MAE_by_bond={bond['mae_kJ_mol']:.9f}  R2_by_bond={r2_display}")
    print("Identity rV=2/(group-10):", result["identity"])
    print(result["scope"])


if __name__ == "__main__":
    main()
