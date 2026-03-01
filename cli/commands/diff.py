import click
import subprocess


@click.command(name="diff")
def diff_cmd():

    result = subprocess.run(
        ["git", "diff", "--name-only"],
        capture_output=True,
        text=True
    )

    changed_files = result.stdout.splitlines()

    py_files = [
        f for f in changed_files
        if f.endswith(".py")
    ]

    click.echo("Changed Python Files:")

    for file in py_files:
        click.echo(file)