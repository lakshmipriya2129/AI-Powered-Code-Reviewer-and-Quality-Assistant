import tomllib
from pathlib import Path


DEFAULT_CONFIG = {
    "exclude": [],
    "severity_threshold": "info",
    "max_complexity": 10,
    "auto_fix": False
}


def load_config():

    config_path = Path("pyproject.toml")

    if not config_path.exists():
        return DEFAULT_CONFIG

    with open(config_path, "rb") as f:
        data = tomllib.load(f)

    return {
        **DEFAULT_CONFIG,
        **data.get("tool", {})
            .get("codeguard", {})
    }


def is_excluded(path, config):

    for ex in config["exclude"]:
        if ex in str(path):
            return True
    return False