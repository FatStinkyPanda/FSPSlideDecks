from backend.deck_manager import initialize_deck_dir, list_decks
from backend.generator import create_basic_deck
from backend.validator import validate_pptx
import sys

def test_workflow():
    print("--- Starting FSPSlideDecks Verification ---")
    
    deck_name = "Verification_Test_Deck"
    print(f"1. Initializing deck project: {deck_name}")
    try:
        path = initialize_deck_dir(deck_name, {"purpose": "verification"})
        print(f"   Success: Created at {path}")
    except FileExistsError:
        print(f"   Note: {deck_name} already exists, proceeding.")
    
    slides = [
        {"title": "Welcome to FSPSlideDecks", "content": "Automated slide generation for AI agents."},
        {"title": "Automated Validation", "content": "Checking for quality and consistency."}
    ]
    
    print("2. Generating PPTX file...")
    output_file = create_basic_deck(deck_name, slides)
    print(f"   Success: File generated at {output_file}")
    
    print("3. Running validation...")
    results = validate_pptx(output_file)
    print(f"   Validation Results: {results}")
    
    if results['valid']:
        print("--- Verification Successful ---")
    else:
        print("--- Verification Failed ---")
        sys.exit(1)

if __name__ == "__main__":
    test_workflow()
