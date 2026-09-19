"""Create the deterministic demonstration data bundled with Figure 23.

The simulator mirrors the visual evaluation in FunDiff Figure 2, but it does
not contain model outputs or recovered paper data. Replace the generated CSVs
with fitted parameters and worst-case curves from an actual generative model
when using this template for an experiment.
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
SEED = 20260427
TRAINING_SIZES = (16, 32, 64, 128, 256)
SAMPLES_PER_SIZE = 1024
TARGETS = {
    "amplitude": (0.5, 1.0),
    "damping": (2.0, 4.0),
    "frequency": (6 * np.pi, 8 * np.pi),
    "shift": (-0.5, 0.5),
}


def _recovering_distribution(rng: np.random.Generator, low: float, high: float,
                             quality: float, shape: tuple[float, float]) -> np.ndarray:
    """Interpolate from a biased beta law to the target uniform law."""
    uniform = rng.uniform(0.0, 1.0, SAMPLES_PER_SIZE)
    biased = rng.beta(shape[0], shape[1], SAMPLES_PER_SIZE)
    choose_uniform = rng.random(SAMPLES_PER_SIZE) < quality
    unit = np.where(choose_uniform, uniform, biased)
    return low + (high - low) * unit


def _unit_residual(rng: np.random.Generator, x: np.ndarray) -> np.ndarray:
    phase = rng.uniform(0, 2 * np.pi)
    residual = (
        0.72 * np.sin(10 * np.pi * x + phase)
        + 0.38 * np.sin(23 * np.pi * x - 0.4 * phase)
        + 0.20 * rng.normal(size=x.size)
    )
    residual -= residual.mean()
    return residual / np.sqrt(np.mean(residual**2))


def main() -> None:
    rng = np.random.default_rng(SEED)
    DATA.mkdir(exist_ok=True)
    parameter_rows: list[dict[str, object]] = []
    curve_rows: list[dict[str, object]] = []
    shapes = {
        "amplitude": (5.0, 3.2),
        "damping": (2.2, 5.0),
        "frequency": (4.8, 4.8),
        "shift": (3.8, 2.0),
    }
    x = np.linspace(0.0, 1.0, 128)

    for index, train_n in enumerate(TRAINING_SIZES):
        quality = (0.10, 0.28, 0.52, 0.76, 0.94)[index]
        values = {
            key: _recovering_distribution(rng, *bounds, quality, shapes[key])
            for key, bounds in TARGETS.items()
        }
        median_mse = (4.5e-3, 2.5e-3, 1.2e-3, 5.5e-4, 2.4e-4)[index]
        mse = rng.lognormal(mean=np.log(median_mse), sigma=0.58, size=SAMPLES_PER_SIZE)

        for sample_id in range(SAMPLES_PER_SIZE):
            parameter_rows.append({
                "train_n": train_n,
                "sample_id": sample_id,
                "amplitude": f"{values['amplitude'][sample_id]:.8f}",
                "damping": f"{values['damping'][sample_id]:.8f}",
                "frequency": f"{values['frequency'][sample_id]:.8f}",
                "shift": f"{values['shift'][sample_id]:.8f}",
                "mse": f"{mse[sample_id]:.10f}",
            })

        worst = int(np.argmax(mse))
        a = values["amplitude"][worst]
        gamma = values["damping"][worst]
        omega = values["frequency"][worst]
        shift = values["shift"][worst]
        reconstructed = a * np.exp(-gamma * x) * np.sin(omega * x) + shift
        generated = reconstructed + np.sqrt(mse[worst]) * _unit_residual(rng, x)
        for t, y, y_fit in zip(x, generated, reconstructed):
            curve_rows.append({
                "train_n": train_n,
                "time": f"{t:.8f}",
                "generated": f"{y:.8f}",
                "reconstructed": f"{y_fit:.8f}",
            })

    with (DATA / "figure23_parameters.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(parameter_rows[0]))
        writer.writeheader()
        writer.writerows(parameter_rows)
    with (DATA / "figure23_curves.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(curve_rows[0]))
        writer.writeheader()
        writer.writerows(curve_rows)


if __name__ == "__main__":
    main()
