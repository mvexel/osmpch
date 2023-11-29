import xml.etree.ElementTree as ET


def parse_xml(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    changesets = []

    # Iterate over each changeset element
    for changeset in root.findall("changeset"):
        changeset_data = changeset.attrib  # Extract attributes

        # Handle tag sub-elements
        for tag in changeset.findall("tag"):
            key = tag.find("key").text
            value = tag.find("value").text
            changeset_data[key] = value  # Flatten the tag structure

        changesets.append(changeset_data)

    return changesets
