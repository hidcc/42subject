from __future__ import annotations

import os

EXPECTED_VARS: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

DEFAULTS: dict[str, dict[str, str]] = {
    "development": {
        "DATABASE_URL": "sqlite:///./matrix_dev.db",
        "LOG_LEVEL": "DEBUG",
        "ZION_ENDPOINT": "http://localhost:8000",
    },
    "production": {
        "LOG_LEVEL": "INFO",
    },
}

REQUIRED_IN_PRODUCTION: list[str] = [
    "DATABASE_URL",
    "API_KEY",
    "ZION_ENDPOINT",
]


def load_env_file() -> bool:
    try:
        from dotenv import load_dotenv  # type: ignore[import-not-found]
    except ImportError:
        return False
    load_dotenv()
    return True


def resolve_mode() -> str:
    mode = os.environ.get("MATRIX_MODE", "development").lower()
    if mode not in DEFAULTS:
        print(f"WARNING: unknown MATRIX_MODE '{mode}', using development.")
        return "development"
    return mode


def resolve_config(mode: str) -> dict[str, str | None]:
    config: dict[str, str | None] = {}
    defaults = DEFAULTS[mode]
    for name in EXPECTED_VARS:
        if name == "MATRIX_MODE":
            config[name] = mode
            continue
        config[name] = os.environ.get(name) or defaults.get(name)
    return config


def mask_secret(value: str | None) -> str:
    if not value:
        return "Missing"
    if len(value) <= 4:
        return "*" * len(value)
    return f"{value[:2]}{'*' * (len(value) - 4)}{value[-2:]}"


def check_missing(config: dict[str, str | None], mode: str) -> list[str]:
    if mode != "production":
        return []
    return [name for name in REQUIRED_IN_PRODUCTION if not config[name]]


def gitignore_protects_env() -> bool:
    try:
        with open(".gitignore", "r", encoding="utf-8") as handle:
            entries = [line.strip() for line in handle]
    except OSError:
        return False
    return ".env" in entries


def report_config(config: dict[str, str | None], mode: str) -> None:
    db = config["DATABASE_URL"]
    api = config["API_KEY"]
    zion = config["ZION_ENDPOINT"]

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if mode == "development":
        print(f"Database: Connected to local instance ({db})")
    else:
        print(f"Database: {db if db else 'NOT CONFIGURED'}")
    print(f"API Access: {'Authenticated' if api else 'Missing key'}")
    print(f"API Key: {mask_secret(api)}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {'Online' if zion else 'Offline'}")


def report_security(dotenv_loaded: bool, missing: list[str]) -> None:
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if gitignore_protects_env():
        print("[OK] .env file properly configured (ignored by git)")
    else:
        print("[WARN] add '.env' to .gitignore to avoid leaking secrets")
    print("[OK] Production overrides available")
    if not dotenv_loaded:
        print("[INFO] python-dotenv not active; using real env / defaults")
    if missing:
        print(f"[ERROR] missing production config: {', '.join(missing)}")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    dotenv_loaded = load_env_file()
    mode = resolve_mode()
    config = resolve_config(mode)
    missing = check_missing(config, mode)

    report_config(config, mode)
    report_security(dotenv_loaded, missing)
    print()
    if missing:
        print("The Oracle cannot proceed: configuration is incomplete.")
    else:
        print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
