"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """EDGAR ETL."""
    # print("EDGAR ETL")
    # print("\x1b[1;32mEDGAR ETL\x1b[0m")
    msg = "EDGAR ETL"
    click.echo(f"\x1b[1;36mInfo:\x1b[0m \x1b[1;32m{msg}\x1b[0m")


if __name__ == "__main__":
    main(prog_name="edgar-etl")  # pragma: no cover
