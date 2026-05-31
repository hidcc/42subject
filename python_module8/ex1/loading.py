from __future__ import annotations

import importlib
import importlib.metadata as metadata
from typing import Any

REQUIRED: list[str] = ["pandas", "numpy", "matplotlib"]

DESCRIPTIONS: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}

OUTPUT_IMAGE: str = "matrix_analysis.png"
DATA_POINTS: int = 1000


def package_version(name: str) -> str | None:
    try:
        return metadata.version(name)
    except metadata.PackageNotFoundError:
        return None


def report_dependencies() -> list[str]:
    print("Checking dependencies:")
    missing: list[str] = []
    for name in REQUIRED:
        version = package_version(name)
        if version is None:
            missing.append(name)
            print(f"[MISSING] {name} - not installed")
        else:
            print(f"[OK] {name} ({version}) - {DESCRIPTIONS[name]}")
    return missing


def print_install_help(missing: list[str]) -> None:
    print()
    print(f"Cannot load programs: missing {', '.join(missing)}.")
    print("Choose one dependency manager to install them:")
    print()
    print("Using pip (reads requirements.txt):")
    print("  python3 -m venv matrix_env")
    print("  source matrix_env/bin/activate")
    print("  pip install -r requirements.txt")
    print()
    print("Using Poetry (reads pyproject.toml):")
    print("  poetry install")
    print("  poetry run python loading.py")


def simulate_matrix_data(np: Any) -> Any:
    rng = np.random.default_rng(seed=42)
    time = np.linspace(0.0, 100.0, DATA_POINTS)
    base_signal = np.sin(time / 5.0) * 50.0 + 100.0
    noise = rng.normal(loc=0.0, scale=10.0, size=DATA_POINTS)
    activity = base_signal + noise
    agents = rng.integers(low=0, high=100, size=DATA_POINTS)
    return time, activity, agents


def build_dataframe(pd: Any, time: Any, activity: Any, agents: Any) -> Any:
    return pd.DataFrame(
        {
            "time": time,
            "activity": activity,
            "agents": agents,
        }
    )


def analyze(df: Any) -> None:
    print(f"Processing {len(df)} data points...")
    mean_activity = df["activity"].mean()
    peak_activity = df["activity"].max()
    busy_agents = int((df["agents"] > 50).sum())
    print(f"  Mean activity : {mean_activity:.2f}")
    print(f"  Peak activity : {peak_activity:.2f}")
    print(f"  Busy agents   : {busy_agents}")


def render_visualization(plt: Any, df: Any) -> None:
    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["time"], df["activity"], color="#00ff41", linewidth=1.0)
    ax.set_title("Matrix Data Stream Analysis")
    ax.set_xlabel("Time")
    ax.set_ylabel("Activity level")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_IMAGE, dpi=100)
    plt.close(fig)


def run_analysis() -> None:
    np: Any = importlib.import_module("numpy")
    pd: Any = importlib.import_module("pandas")
    matplotlib: Any = importlib.import_module("matplotlib")
    matplotlib.use("Agg")
    plt: Any = importlib.import_module("matplotlib.pyplot")

    print("Analyzing Matrix data...")
    time, activity, agents = simulate_matrix_data(np)
    df = build_dataframe(pd, time, activity, agents)
    analyze(df)
    render_visualization(plt, df)
    print()
    print("Analysis complete!")
    print(f"Results saved to: {OUTPUT_IMAGE}")


def compare_pip_and_poetry() -> None:
    print("pip vs Poetry:")
    print("  pip      : installs from requirements.txt; versions are")
    print("             flat and not locked by default.")
    print("  Poetry   : reads pyproject.toml, resolves a dependency")
    print("             tree and writes an exact poetry.lock file.")
    print("  Installed versions seen by this interpreter:")
    for name in REQUIRED:
        version = package_version(name) or "not installed"
        print(f"    - {name}: {version}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()
    missing = report_dependencies()
    if missing:
        print_install_help(missing)
        return
    print()
    run_analysis()
    print()
    compare_pip_and_poetry()


if __name__ == "__main__":
    main()
