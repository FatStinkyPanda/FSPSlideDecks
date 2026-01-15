from typing import Dict, List
import json

from .deck_manager import initialize_deck_dir, list_decks, get_deck_path
from .generator import create_enhanced_deck
from .validator import validate_pptx

class SlideDeckMCPTools:
    """
    Standard interface for AI agents to interact with the Slide Deck Backend.
    These methods are designed to be wrapped as MCP tools.
    """

    @staticmethod
    def create_deck(deck_name: str, purpose: str = "") -> str:
        """
        Initializes a new isolated slide deck project folder.
        """
        try:
            path = initialize_deck_dir(deck_name, {"purpose": purpose})
            return f"Success: Deck '{deck_name}' initialized at {path}"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def generate_slides(deck_name: str, slides: List[Dict[str, str]]) -> str:
        """
        Generates or updates a PPTX file with the provided slide content.
        'slides' should be a list of {'title': '...', 'content': '...'}.
        """
        try:
            output_file = create_enhanced_deck(deck_name, slides)
            return f"Success: Slide deck generated at {output_file}"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def validate_deck(deck_name: str) -> str:
        """
        Performs quality and structural validation on the generated deck.
        """
        try:
            deck_path = get_deck_path(deck_name)
            output_file = deck_path / "output" / f"{deck_name}.pptx"
            results = validate_pptx(output_file)
            return json.dumps(results, indent=2)
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def list_all_decks() -> str:
        """
        Lists all existing slide deck projects.
        """
        decks = list_decks()
        return json.dumps(decks)
