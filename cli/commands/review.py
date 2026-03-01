import click
from parser.analyzer import analyze_file
from ai_review.reviewer import AIReviewer
from cli.config import load_config


@click.command(name="review")
@click.argument("file")
def review_cmd(file):

    config = load_config()

    analysis = analyze_file(file)

    reviewer = AIReviewer()

    review = reviewer.generate_review(
        file,
        analysis.smells
    )

    threshold = config["severity_threshold"]

    levels = ["info", "warning", "critical"]

    for issue in review.issues:
        if levels.index(issue.severity) >= \
           levels.index(threshold):

            click.echo(
                f"[{issue.severity.upper()}]"
                f" {issue.title}"
            )