import subprocess


def get_staged_files():
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True,
        text=True
    )

    files = result.stdout.splitlines()

    return [
        f for f in files
        if f.endswith(".py")
    ]