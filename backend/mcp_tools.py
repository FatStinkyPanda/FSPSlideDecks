from typing import Dict, List
import json

from .deck_manager import initialize_deck_dir, list_decks, get_deck_path, clone_deck
from .generator import create_enhanced_deck, add_image_slide, add_slide_to_deck, delete_slide_from_deck
from .distributor import package_assets, export_to_pdf
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
    def clone_existing_deck(source_deck: str, target_deck: str) -> str:
        """
        Clones an existing deck to a new one, including all assets.
        """
        try:
            path = clone_deck(source_deck, target_deck)
            return f"Success: Deck '{source_deck}' cloned to '{target_deck}' at {path}"
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
    def add_image_to_deck(deck_name: str, title: str, image_filename: str) -> str:
        """
        Adds a slide with an image from the assets folder to the deck.
        """
        try:
            output_file = add_image_slide(deck_name, title, image_filename)
            return f"Success: Image slide added to {output_file}"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def append_slide(deck_name: str, title: str, content: str = "", layout: int = 1) -> str:
        """
        Appends a single slide to the deck.
        """
        try:
            slide_data = {"title": title, "content": content, "layout": layout}
            output_file = add_slide_to_deck(deck_name, slide_data)
            return f"Success: Slide added to {output_file}"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def remove_slide(deck_name: str, index: int) -> str:
        """
        Removes a slide from the deck by its index.
        """
        try:
            output_file = delete_slide_from_deck(deck_name, index)
            return f"Success: Slide {index} removed from {output_file}"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def distribute_deck(deck_name: str, destination_dir: str) -> str:
        """
        Packages the deck and its assets for distribution.
        """
        try:
            dest_path = Path(destination_dir)
            dist_path = package_assets(deck_name, dest_path)
            return f"Success: Deck packaged at {dist_path}"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def export_pdf(deck_name: str) -> str:
        """
        Exports the deck to a PDF format.
        """
        try:
            pdf_path = export_to_pdf(deck_name)
            return f"Success: PDF exported to {pdf_path}"
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def list_all_decks() -> str:
        """
        Lists all existing slide deck projects.
        """
        decks = list_decks()
        return json.dumps(decks)
