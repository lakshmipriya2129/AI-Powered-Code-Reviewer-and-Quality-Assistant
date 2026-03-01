import click
from ai_review.reviewer import AIReviewer
from cli.config import load_config


@click.command(name="apply")
@click.argument("file")
def apply_cmd(file):

    config = load_config()

    if not config["auto_fix"]:
        click.echo(" Auto-fix disabled")
        return

    reviewer = AIReviewer()

    reviewer.auto_fix(file)

    click.echo(f" Fix applied → {file}")