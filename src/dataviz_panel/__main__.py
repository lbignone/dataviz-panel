"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Dataviz Panel."""


if __name__ == "__main__":
    main(prog_name="dataviz-panel")  # pragma: no cover
