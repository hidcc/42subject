import os
import site
import sys


def in_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix or hasattr(sys, "real_prefix")


def site_packages_path() -> str:
    try:
        packages = site.getsitepackages()
    except AttributeError:
        packages = []
    return packages[0] if packages else "unknown"


def report_inside() -> None:
    raw_env = os.environ.get("VIRTUAL_ENV", sys.prefix)
    env_name = os.path.basename(raw_env.rstrip("/"))

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {sys.prefix}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(site_packages_path())


def report_outside() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("Global package location:")
    print(site_packages_path())
    print()
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate   # On Unix")
    print("matrix_env\\Scripts\\activate    # On Windows")
    print()
    print("Then run this program again.")


def main() -> None:
    if in_virtual_env():
        report_inside()
    else:
        report_outside()


if __name__ == "__main__":
    main()
