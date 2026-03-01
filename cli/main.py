import click

from cli.commands.scan import scan_cmd
from cli.commands.review import review_cmd
from cli.commands.apply import apply_cmd
from cli.commands.report import report_cmd
from cli.commands.diff import diff_cmd


@click.group()
def cli():
    """
    CodeGuard CLI
    AI Powered Code Review Tool
    """
    pass


cli.add_command(scan_cmd)
cli.add_command(review_cmd)
cli.add_command(apply_cmd)
cli.add_command(report_cmd)
cli.add_command(diff_cmd)


if __name__ == "__main__":
    cli()