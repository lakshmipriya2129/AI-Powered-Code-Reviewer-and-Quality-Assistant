import click
from pathlib import Path

from parser.analyzer import analyze_file
from metrics.metrics_engine import MetricsEngine


@click.command(name="report")
@click.argument("path")
def report_cmd(path):

    engine = MetricsEngine()

    files = list(
        Path(path).rglob("*.py")
    )

    analyses = [
        analyze_file(str(f))
        for f in files
    ]

    results = engine.analyze_project(
        files,
        analyses
    )

    csv_file, html_file = \
        engine.export_reports(results)

    click.echo(f"CSV: {csv_file}")
    click.echo(f"HTML: {html_file}")