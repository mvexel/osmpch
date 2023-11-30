import time
import click
from osmpch.config import BATCH_SIZE
from osmpch.reader import read_xml
from osmpch.utils.osm import get_latest_osm_changeset_id
from writers import get_writer
import humanize


@click.group()
def main():
    """OSM PCH Command Line Interface"""
    pass


@main.command()
# requires a filepath argument
@click.argument("filepath", type=click.Path(exists=True))
# option to specify the writer, default csv, other options are sqlite, postgresql
@click.option(
    "--writer", type=click.Choice(["csv", "sqlite", "postgresql"]), default="csv"
)
def process(filepath, writer):
    """Process an XML file."""

    if not filepath.endswith(".xml") and not filepath.endswith(".bz2"):
        raise click.BadParameter("File must be a .xml or .bz2 file")

    writer = get_writer(writer)

    changeset_batch = []
    # get latest changeset id from OSM to approximate progress
    latest_changeset_id = get_latest_osm_changeset_id()
    print(f"Latest OSM changeset ID: {latest_changeset_id}")
    start_time = time.time()
    total_changesets_read = 0
    for changeset in read_xml(filepath):
        changeset_batch.append(changeset)
        if len(changeset_batch) == BATCH_SIZE:
            total_changesets_read += len(changeset_batch)
            # print total progress in 2 decimal places percent and expected time to completion
            line = f"Progress: {round(total_changesets_read / latest_changeset_id * 100, 2)}% | Expected time to completion: about {humanize.naturaldelta((time.time() - start_time) / total_changesets_read * (latest_changeset_id - total_changesets_read))}"
            print(
                f"{line:<100}", end="\r"
            )  # ensure that a shorter line does not leave characters from a longer line
            writer.write_changesets(changeset_batch)
            changeset_batch = []


if __name__ == "__main__":
    main()
