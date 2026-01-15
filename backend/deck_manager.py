from pathlib import Path
import json
import shutil

DECKS_DIR = Path(__file__).parent.parent / "decks"

def initialize_deck_dir(deck_name: str, metadata: dict = None) -> Path:
    """Creates a new isolated project folder for a slide deck."""
    deck_path = DECKS_DIR / deck_name

    if deck_path.exists():
        raise FileExistsError(f"Deck '{deck_name}' already exists at {deck_path}")

    # Create structure
    deck_path.mkdir(parents=True)
    (deck_path / "assets").mkdir()
    (deck_path / "output").mkdir()

    # Initialize config
    config = {
        "name": deck_name,
        "status": "initialized",
        "created_at": None, # Should add timestamp logic
        "metadata": metadata or {}
    }

    with open(deck_path / "config.json", "w") as f:
        json.dump(config, f, indent=4)

    return deck_path

def list_decks() -> list:
    """Returns a list of all existing decks."""
    if not DECKS_DIR.exists():
        return []
    return [d.name for d in DECKS_DIR.iterdir() if d.is_dir()]

def get_deck_path(deck_name: str) -> Path:
    """Gets the absolute path to a deck directory."""
    return DECKS_DIR / deck_name

def clone_deck(source_deck: str, target_deck: str) -> Path:
    """Clones an existing deck structure and assets to a new deck."""
    source_path = DECKS_DIR / source_deck
    target_path = DECKS_DIR / target_deck

    if not source_path.exists():
        raise FileNotFoundError(f"Source deck '{source_deck}' not found.")
    if target_path.exists():
        raise FileExistsError(f"Target deck '{target_deck}' already exists.")

    shutil.copytree(source_path, target_path)

    # Update target config
    config_path = target_path / "config.json"
    if config_path.exists():
        with open(config_path, "r") as f:
            config = json.load(f)
        config["name"] = target_deck
        config["cloned_from"] = source_deck
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)

    return target_path

def delete_deck(deck_name: str):
    """Safely removes a deck project folder."""
    deck_path = DECKS_DIR / deck_name
    if deck_path.exists() and deck_path.is_dir():
        shutil.rmtree(deck_path)
    else:
        raise FileNotFoundError(f"Deck '{deck_name}' not found.")
