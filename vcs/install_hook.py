from pathlib import Path


HOOK = """#!/bin/sh
python -m vcs.precommit
"""


def install():

    hook_path = Path(".git/hooks/pre-commit")

    hook_path.write_text(HOOK)

    hook_path.chmod(0o775)

    print(" Pre-commit hook installed")


if __name__ == "__main__":
    install()