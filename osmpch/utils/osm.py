import requests

def get_latest_osm_changeset_id() -> int:
    """Get the latest OSM changeset ID from the OSM API."""
    url = "https://api.openstreetmap.org/api/0.6/changesets.json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    latest_changeset = response.json()["changesets"][-1]
    return latest_changeset["id"]