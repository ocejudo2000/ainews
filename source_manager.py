import json

SOURCES_FILE = "sources.json"

def get_sources():
    """Reads the list of sources from the JSON file."""
    try:
        with open(SOURCES_FILE, "r") as f:
            data = json.load(f)
            return data.get("sources", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def add_source(name, url, type):
    """Adds a new source to the JSON file."""
    sources = get_sources()
    sources.append({"name": name, "url": url, "type": type})
    with open(SOURCES_FILE, "w") as f:
        json.dump({"sources": sources}, f, indent=2)
