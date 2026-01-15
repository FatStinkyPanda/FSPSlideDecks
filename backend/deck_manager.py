import shutil
import json
from pathlib import Path

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

def delete_deck(deck_name: str):
    """Safely removes a deck project folder."""
    deck_path = DECKS_DIR / deck_name
    if deck_path.exists() and deck_path.is_dir():
        shutil.rmtree(deck_path)
    else:
        raise FileNotFoundError(f"Deck '{deck_name}' not found.")
