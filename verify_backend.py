import sys
import sys

from backend.deck_manager import initialize_deck_dir
from backend.generator import create_enhanced_deck
from backend.validator import validate_pptx

def test_workflow():
    print("--- Starting FSPSlideDecks Verification ---")

    deck_name = "Enhanced_Verification_Deck"
    print(f"1. Initializing deck project: {deck_name}")
    try:
        path = initialize_deck_dir(deck_name, {"purpose": "enhanced_verification"})
        print(f"   Success: Created at {path}")
    except FileExistsError:
        print(f"   Note: {deck_name} already exists, proceeding.")

    slides = [
        {"title": "Enhanced Slide Generation", "content": "Now supporting multiple layouts and data formats."},
        {
            "title": "Bullet Point Support",
            "layout": 1,
            "bullet_points": [
                "Automated bullet point creation",
                "Clean structural formatting",
                "Level support ready for future"
            ]
        },
        {
            "title": "Alternate Layout Test",
            "layout": 2, # Common Title and Content layout
            "content": "Testing layout index 2 as a valid fallback."
        }
    ]

    print("2. Generating Enhanced PPTX file...")
    output_file = create_enhanced_deck(deck_name, slides)
    print(f"   Success: File generated at {output_file}")

    print("3. Running validation...")
    results = validate_pptx(output_file)
    print(f"   Validation Results: {results}")

    if results['valid'] and results['slide_count'] == 3:
        print("--- Verification Successful ---")
    else:
        print(f"--- Verification Failed (Slide Count: {results['slide_count']}) ---")
        sys.exit(1)

if __name__ == "__main__":
    test_workflow()
