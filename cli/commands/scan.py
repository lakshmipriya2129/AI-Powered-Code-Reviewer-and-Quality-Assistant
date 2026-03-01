import click
from pathlib import Path

from parser.analyzer import analyze_file
from cli.config import load_config, is_excluded


@click.command(name="scan")
@click.argument("path")
def scan_cmd(path):

    config = load_config()

    files = Path(path).rglob("*.py")

    for file in files:

        if is_excluded(file, config):
            continue

        result = analyze_file(str(file))

        click.echo(
            f" Scanned: {file}"
        )
        click.echo(
            f" Functions: {len(result.functions)}"
        )