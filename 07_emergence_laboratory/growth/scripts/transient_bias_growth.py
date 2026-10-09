"""Square-envelope growth with a transient directional field.

Derived from the supplied experiment_seed_independence_crystal.py.
Protocol ordered-frontier-v1 uses sorted candidates; it does not reproduce the
original set-iteration trajectories. Import and default CLI execution write no
files. Supplied tables are immutable observations, not results of this module.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import random
import sys
from pathlib import Path

import numpy as np

PROTOCOL = "ordered-frontier-v1"
NEIGH8 = tuple((dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0))
NEIGH4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
METRICS = ("m2", "q4", "aspect", "compactness", "perimeter")
CONDITIONS = ("no_bias", "transient_bias")
SOURCE_CONDITIONS = {"sin_semilla": "no_bias", "con_semilla": "transient_bias"}
DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def shape_metrics(occupied):
    """Dimensionless shape descriptors, except perimeter in lattice edges."""
    if not occupied:
        raise ValueError("occupied must contain at least one lattice site")
    points = np.asarray(sorted(occupied), dtype=float)
    x, y = points[:, 0], points[:, 1]
    theta = np.arctan2(y - y.mean(), x - x.mean())
    radius = np.hypot(x - x.mean(), y - y.mean())
    mask = radius > 1e-12
    width, height = np.ptp(x) + 1, np.ptp(y) + 1
    perimeter = sum((px + dx, py + dy) not in occupied
                    for px, py in occupied for dx, dy in NEIGH4)
    return {
        "m2": float(np.mean(np.cos(2 * theta[mask]))) if mask.any() else 0.0,
        "q4": float(abs(np.mean(np.exp(4j * theta[mask])))) if mask.any() else 0.0,
        "aspect": float(max(width, height) / min(width, height)),
        "compactness": float(len(occupied) / (width * height)),
        "perimeter": float(perimeter),
    }


def bias_amplitude(step, strength, decay_tau, cutoff=None):
    """step counts additions, with step=1 selecting the second occupied site."""
    if step < 1 or decay_tau <= 0 or not math.isfinite(decay_tau):
        raise ValueError("step must be positive and decay_tau finite and positive")
    if not math.isfinite(strength) or (cutoff is not None and (
            not isinstance(cutoff, int) or isinstance(cutoff, bool) or cutoff < 1)):
        raise ValueError("strength must be finite and cutoff a positive integer step")
    if cutoff is not None and step >= cutoff:
        return 0.0
    return strength * math.exp(-step / decay_tau)


def grow(n_sites=400, seed=1000, strength=0.0, decay_tau=37.5, beta=3.0,
         cutoff=None, checkpoints=None):
    """Add sites until n_sites, not until an equilibrium criterion is met.

    Score: -Chebyshev radius + .35*eight-neighbour bonds + bias*cos(2*theta).
    The radius and field use the fixed origin. This is a global radial rule
    alongside a local bond term, not a purely local or atomistic crystal model.
    """
    if not isinstance(n_sites, int) or isinstance(n_sites, bool) or n_sites < 1:
        raise ValueError("n_sites must be a positive integer")
    if not math.isfinite(beta) or beta < 0:
        raise ValueError("beta must be finite and nonnegative")
    bias_amplitude(1, strength, decay_tau, cutoff)
    if checkpoints is None:
        checkpoints = (max(1, n_sites // 8), max(1, n_sites // 4),
                       max(1, n_sites // 2), n_sites)
    checkpoint_set = set(checkpoints) | {n_sites}
    if any(not isinstance(n, int) or n < 1 or n > n_sites for n in checkpoint_set):
        raise ValueError("checkpoints must be integer site counts within the run")
    rng = random.Random(seed)
    occupied, frontier = {(0, 0)}, set(NEIGH8)
    trace = []
    if 1 in checkpoint_set:
        trace.append({"n": 1, **shape_metrics(occupied)})
    for step in range(1, n_sites):
        candidates = sorted(frontier)
        amplitude = bias_amplitude(step, strength, decay_tau, cutoff)
        scores = []
        for x, y in candidates:
            bonded = sum((x + dx, y + dy) in occupied for dx, dy in NEIGH8)
            scores.append(-max(abs(x), abs(y)) + 0.35 * bonded
                          + amplitude * math.cos(2 * math.atan2(y, x)))
        weights = np.exp(beta * (np.asarray(scores) - max(scores)))
        threshold, cumulative = rng.random() * float(weights.sum()), 0.0
        chosen = candidates[-1]
        for candidate, weight in zip(candidates, weights):
            cumulative += float(weight)
            if cumulative >= threshold:
                chosen = candidate
                break
        frontier.remove(chosen)
        occupied.add(chosen)
        for dx, dy in NEIGH8:
            candidate = (chosen[0] + dx, chosen[1] + dy)
            if candidate not in occupied:
                frontier.add(candidate)
        if len(occupied) in checkpoint_set:
            trace.append({"n": len(occupied), **shape_metrics(occupied)})
    return occupied, trace, shape_metrics(occupied)


def paired_bootstrap(a, b, reps=4000, seed=42):
    """Percentile CI for mean(b-a), resampling whole matched runs."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    if a.ndim != 1 or b.shape != a.shape or a.size < 2:
        raise ValueError("at least two equally sized one-dimensional paired samples required")
    if not np.all(np.isfinite(a)) or not np.all(np.isfinite(b)):
        raise ValueError("samples must be finite")
    if not isinstance(reps, int) or reps < 1:
        raise ValueError("reps must be a positive integer")
    differences = b - a
    rng = np.random.default_rng(seed)
    # Each bootstrap row selects pair IDs, preserving within-pair dependence.
    indices = rng.integers(0, len(a), size=(reps, len(a)))
    low, median, high = np.quantile(differences[indices].mean(axis=1), [0.025, 0.5, 0.975])
    return {"difference_mean": float(differences.mean()), "ci95_low": float(low),
            "bootstrap_median": float(median), "ci95_high": float(high)}


def _paired_rows(final_rows):
    rows = {}
    for row in final_rows:
        key = (row["condition"], row["run"])
        if key in rows:
            raise ValueError(f"duplicate final row: {key}")
        if row["condition"] not in CONDITIONS:
            raise ValueError(f"unknown condition: {row['condition']}")
        if any(not math.isfinite(float(row[m])) for m in METRICS):
            raise ValueError("all metrics must be finite")
        rows[key] = row
    ids = sorted(run for condition, run in rows if condition == CONDITIONS[0])
    if set(ids) != {run for condition, run in rows if condition == CONDITIONS[1]}:
        raise ValueError("condition run IDs do not match")
    if len(ids) < 2:
        raise ValueError("at least two complete pairs required")
    return [[rows[(condition, run)] for run in ids] for condition in CONDITIONS]


def compare_pairs(final_rows, reps=4000, seed=42):
    a_rows, b_rows = _paired_rows(final_rows)
    result = []
    for metric in METRICS:
        a = np.asarray([r[metric] for r in a_rows], dtype=float)
        b = np.asarray([r[metric] for r in b_rows], dtype=float)
        result.append({"metric": metric, "no_bias_mean": float(a.mean()),
                       "transient_bias_mean": float(b.mean()),
                       **paired_bootstrap(a, b, reps, seed)})
    return result


def trace_summary(trace_rows):
    grouped = {}
    for row in trace_rows:
        grouped.setdefault((row["condition"], row["n"]), []).append(row)
    result = []
    for (condition, n), rows in sorted(grouped.items()):
        m2 = np.asarray([row["m2"] for row in rows], dtype=float)
        result.append({"condition": condition, "n": n, "runs": len(rows),
                       "m2_signed_mean": float(m2.mean()),
                       "m2_mean_absolute": float(np.abs(m2).mean()),
                       "m2_rms": float(np.sqrt(np.mean(m2 ** 2))),
                       "q4_mean": float(np.mean([row["q4"] for row in rows]))})
    return result


def experiment(n_runs=8, n_sites=400, seed=1000, strength=6.0, decay_tau=37.5,
               beta=3.0, cutoff=None, reps=2000, bootstrap_seed=42):
    if not isinstance(n_runs, int) or isinstance(n_runs, bool) or n_runs < 2:
        raise ValueError("n_runs must be an integer >=2")
    final_rows, trace_rows, microstates = [], [], {}
    for condition, amplitude in ((CONDITIONS[0], 0.0), (CONDITIONS[1], strength)):
        microstates[condition] = []
        for run in range(n_runs):
            occupied, trace, final = grow(n_sites, seed + run, amplitude, decay_tau,
                                         beta, cutoff)
            final_rows.append({"condition": condition, "run": run, **final})
            trace_rows.extend({"condition": condition, "run": run, **r} for r in trace)
            microstates[condition].append(sorted(occupied))
    diagnostics = []
    for run, (a, b) in enumerate(zip(microstates[CONDITIONS[0]], microstates[CONDITIONS[1]])):
        a, b = set(a), set(b)
        diagnostics.append({"run": run, "jaccard": len(a & b) / len(a | b),
                            "exact_equal": a == b})
    config = dict(n_runs=n_runs, n_sites=n_sites, seed=seed, strength=strength,
                  decay_tau=decay_tau, beta=beta, cutoff=cutoff, reps=reps,
                  bootstrap_seed=bootstrap_seed)
    return {
        "summary": {
            "kind": "new_ordered_frontier_experiment", "protocol": PROTOCOL,
            "config": config, "python": platform.python_version(), "numpy": np.__version__,
            "pairing": "same random.Random(seed+run) stream in both conditions",
            "stopping_rule": "fixed site count, not equilibrium",
            "comparison": compare_pairs(final_rows, reps, bootstrap_seed),
            "trace_summary": trace_summary(trace_rows),
            "microstate_jaccard_mean": float(np.mean([d["jaccard"] for d in diagnostics])),
            "exact_equal_pairs": sum(d["exact_equal"] for d in diagnostics),
        },
        "final_rows": final_rows, "trace_rows": trace_rows,
        "microstates": microstates, "pair_diagnostics": diagnostics,
    }


def _read_csv(path):
    with Path(path).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def _parse_source_rows(path, with_n=False):
    rows = []
    for row in _read_csv(path):
        if row["condition"] not in SOURCE_CONDITIONS:
            raise ValueError("unknown supplied condition")
        parsed = {"condition": SOURCE_CONDITIONS[row["condition"]], "run": int(row["run"]),
                  **{metric: float(row[metric]) for metric in METRICS}}
        if with_n:
            parsed["n"] = int(row["n"])
        rows.append(parsed)
    return rows


def reanalyze_supplied(data_dir=DATA_DIR, reps=4000, seed=42):
    """Read source CSVs and validate IDs, endpoints and published means."""
    data_dir = Path(data_dir)
    paths = {key: data_dir / filename for key, filename in (
        ("trace", "supplied_growth_trace.csv"), ("final", "supplied_final_runs.csv"),
        ("legacy_comparison", "supplied_unpaired_comparison.csv"))}
    final_rows = _parse_source_rows(paths["final"])
    trace_rows = _parse_source_rows(paths["trace"], with_n=True)
    paired = _paired_rows(final_rows)
    expected_runs = set(range(40))
    if any({r["run"] for r in group} != expected_runs for group in paired):
        raise ValueError("supplied experiment must contain runs 0..39 in each condition")
    checkpoints = {50, 100, 200, 400, 800, 1600, 3200}
    indexed = {}
    for row in trace_rows:
        key = (row["condition"], row["run"], row["n"])
        if key in indexed or any(not math.isfinite(row[m]) for m in METRICS):
            raise ValueError("duplicate or nonfinite trace row")
        indexed[key] = row
    expected_keys = {(c, r, n) for c in CONDITIONS for r in expected_runs for n in checkpoints}
    if set(indexed) != expected_keys:
        raise ValueError("supplied trace has unexpected or missing run/checkpoint keys")
    for row in final_rows:
        end = indexed[(row["condition"], row["run"], 3200)]
        if any(not math.isclose(row[m], end[m], rel_tol=0, abs_tol=1e-12) for m in METRICS):
            raise ValueError("final row does not match last checkpoint")
    comparison = compare_pairs(final_rows, reps, seed)
    legacy = _read_csv(paths["legacy_comparison"])
    if len(legacy) != len(METRICS) or {r["metric"] for r in legacy} != set(METRICS):
        raise ValueError("legacy comparison metric keys do not match")
    for row in legacy:
        current = next(r for r in comparison if r["metric"] == row["metric"])
        for old, new in (("sin_semilla_mean", "no_bias_mean"),
                         ("con_semilla_mean", "transient_bias_mean"),
                         ("difference", "difference_mean")):
            if not math.isclose(float(row[old]), current[new], rel_tol=0, abs_tol=1e-12):
                raise ValueError("legacy comparison means do not match final data")
    return {"summary": {
        "kind": "paired_reanalysis_of_supplied_tables",
        "source_protocol": "original frontier set iteration; not ordered-frontier-v1",
        "source_rows": {"final": len(final_rows), "trace": len(trace_rows), "pairs": 40},
        "source_sha256": {key: hashlib.sha256(path.read_bytes()).hexdigest()
                          for key, path in paths.items()},
        "checks": "unique matched IDs, all seven checkpoints, endpoint equality, legacy means",
        "bootstrap": {"method": "paired percentile", "reps": reps, "seed": seed},
        "comparison": comparison, "trace_summary": trace_summary(trace_rows),
        "microstates_available": False,
        "microstate_note": "Original Jaccard and exact-equality claims cannot be reconstructed from CSV descriptors.",
        "inference_scope": "Exploratory; no pre-specified equivalence margin or simultaneous-coverage correction.",
    }}


def write_outputs(result, output_dir):
    """Only explicit CLI opt-in writes outputs; existing files are not replaced."""
    destination = Path(output_dir)
    files = {"summary.json": result["summary"]}
    if "microstates" in result:
        files["microstates.json"] = result["microstates"]
    tables = {}
    for key, filename in (("final_rows", "final_runs.csv"), ("trace_rows", "growth_trace.csv"),
                          ("pair_diagnostics", "pair_diagnostics.csv")):
        if key in result:
            tables[filename] = result[key]
    tables["paired_comparison.csv"] = result["summary"]["comparison"]
    tables["trace_summary.csv"] = result["summary"]["trace_summary"]
    if any((destination / name).exists() for name in (*files, *tables)):
        raise FileExistsError("output files already exist; choose a new output directory")
    destination.mkdir(parents=True, exist_ok=True)
    for filename, content in files.items():
        with (destination / filename).open("x", encoding="utf-8") as stream:
            json.dump(content, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
    for filename, rows in tables.items():
        with (destination / filename).open("x", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reanalyze-supplied", action="store_true",
                        help="validate source CSVs and recalculate paired intervals; no growth run")
    parser.add_argument("--data-dir", type=Path, default=DATA_DIR)
    parser.add_argument("--n-runs", type=int, default=8, help="number of matched pairs")
    parser.add_argument("--n-sites", type=int, default=400)
    parser.add_argument("--seed", type=int, default=1000)
    parser.add_argument("--strength", type=float, default=6.0)
    parser.add_argument("--decay-tau", type=float, default=37.5,
                        help="quick default scales source tau=300 by 400/3200")
    parser.add_argument("--beta", type=float, default=3.0)
    parser.add_argument("--cutoff", type=int, help="field exactly zero for addition step >= cutoff")
    parser.add_argument("--bootstrap-reps", type=int, default=4000)
    parser.add_argument("--bootstrap-seed", type=int, default=42)
    parser.add_argument("--output-dir", type=Path, help="explicit output opt-in; never replaces files")
    args = parser.parse_args(argv)
    try:
        if args.reanalyze_supplied:
            result = reanalyze_supplied(args.data_dir, args.bootstrap_reps, args.bootstrap_seed)
        else:
            result = experiment(args.n_runs, args.n_sites, args.seed, args.strength,
                                args.decay_tau, args.beta, args.cutoff,
                                args.bootstrap_reps, args.bootstrap_seed)
        if args.output_dir is not None:
            write_outputs(result, args.output_dir)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
