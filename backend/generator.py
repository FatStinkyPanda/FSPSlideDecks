from pptx import Presentation
from pathlib import Path
from .deck_manager import get_deck_path

def create_basic_deck(deck_name: str, slides_content: list) -> Path:
    """
    Generates a PPTX file based on provided content.
    slides_content: list of dicts like {'title': '...', 'content': '...'}
    """
    deck_path = get_deck_path(deck_name)
    if not deck_path.exists():
        raise FileNotFoundError(f"Deck folder '{deck_name}' does not exist.")
    
    prs = Presentation()
    
    for slide_data in slides_content:
        # Use simple layout for now (Title and Content)
        slide_layout = prs.slide_layouts[1] 
        slide = prs.slides.add_slide(slide_layout)
        
        title = slide.shapes.title
        content = slide.placeholders[1]
        
        title.text = slide_data.get('title', 'Untitled Slide')
        content.text = slide_data.get('content', '')
    
    output_file = deck_path / "output" / f"{deck_name}.pptx"
    prs.save(output_file)
    
    return output_file

def add_image_slide(deck_name: str, title_text: str, image_filename: str) -> Path:
    """Adds a slide with an image from the assets folder."""
    deck_path = get_deck_path(deck_name)
    image_path = deck_path / "assets" / image_filename
    
    if not image_path.exists():
        raise FileNotFoundError(f"Asset '{image_filename}' not found in {deck_name}/assets")
        
    prs = Presentation() # Note: This currently overwrites or needs a load mechanism for true "adding"
    # For now, let's keep it simple: functions that create/manipulate presentations.
    # Future enhancement: load existing presentation if it exists.
    
    # ... placeholder for more complex logic ...
    return deck_path / "output" / f"{deck_name}_temp.pptx"
