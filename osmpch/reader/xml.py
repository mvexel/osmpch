import bz2

from defusedxml import ElementTree as ET
from iso8601 import parse_date

from osmpch.models import Changeset


def read_xml(file_path):
    """Read an XML file and yield the data.

    Args:
        file_path (str): Path to the XML file to read.
    """

    # We already checked that the file exists in the CLI and that it is a .xml or .bz2 file
    if file_path.endswith(".bz2"):
        opener = bz2.open
    else:
        opener = open

    with opener(file_path, "rb") as file:
        context = ET.iterparse(file, events=("start", "end"))
        context = iter(context)
        event, root = next(context)

        for event, elem in context:
            if event == "end" and elem.tag == "changeset":
                # Extract tags and convert them into the format expected by the ORM (if necessary)
                tags = {tag.get("k"): tag.get("v") for tag in elem.findall("tag")}

                changeset_attributes = elem.attrib
                changeset_attributes["tags"] = tags

                # Rename some attributes because of ...historical reasons
                if "num_changes" in changeset_attributes:
                    changeset_attributes["changes_count"] = changeset_attributes.pop(
                        "num_changes"
                    )
                if "num_comments" in changeset_attributes:
                    changeset_attributes["comments_count"] = changeset_attributes.pop(
                        "num_comments"
                    )

                # parse created_at and closed_at which are ISO 8601 formatted strings as proper python datetimes
                changeset_attributes["created_at"] = parse_date(
                    changeset_attributes["created_at"]
                )
                if "closed_at" in changeset_attributes:
                    changeset_attributes["closed_at"] = parse_date(
                        changeset_attributes["closed_at"]
                    )

                # convert open attribute to boolean
                changeset_attributes["open"] = changeset_attributes["open"] == "true"

                changeset = Changeset(**changeset_attributes)
                yield changeset

                root.clear()
