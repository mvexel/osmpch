import click
from osmpch.reader import read_xml
# Import converters here


@click.group()
def main():
    """OSM PCH Command Line Interface"""
    pass


@main.command()
# requires a filepath argument
@click.argument("filepath", type=click.Path(exists=True))
@click.option("--writer", default="csv", help="Writer to use")
def process(filepath, converter):
    """Process an XML file."""

    # check that file is a .xml or .bz2 file
    if not filepath.endswith(".xml") and not filepath.endswith(".bz2"):
        raise click.BadParameter("File must be a .xml or .bz2 file")

    # Check that the writer is valid by trying to import it
    try:
        writer = __import__(writer)
    except ImportError:
        raise click.BadParameter("Writer not found")

    # Read the XML file
    data = read_xml(filepath)

if __name__ == "__main__":
    main()
