from pathlib import Path

from .deck_manager import get_deck_path
from pptx import Presentation

def create_enhanced_deck(deck_name: str, slides_content: list) -> Path:
    """
    Generates a PPTX file with support for multiple layouts.
    slides_content: list of dicts like:
    {
        'title': '...',
        'content': '...',
        'layout': 1, # default Title and Content
        'bullet_points': ['...', '...']
    }
    """
    deck_path = get_deck_path(deck_name)
    if not deck_path.exists():
        raise FileNotFoundError(f"Deck folder '{deck_name}' does not exist.")
    
    prs = Presentation()
    
    for slide_data in slides_content:
        layout_idx = slide_data.get('layout', 1)
        if layout_idx >= len(prs.slide_layouts):
            layout_idx = 1 # fallback
            
        slide_layout = prs.slide_layouts[layout_idx]
        slide = prs.slides.add_slide(slide_layout)
        
        # Handle Title
        if slide.shapes.title:
            slide.shapes.title.text = slide_data.get('title', 'Untitled Slide')
        
        # Handle Content / Body
        if len(slide.placeholders) > 1:
            body_shape = slide.placeholders[1]
            tf = body_shape.text_frame
            
            # Simple content text or bullet points
            if 'bullet_points' in slide_data:
                tf.text = slide_data['bullet_points'][0]
                for bp in slide_data['bullet_points'][1:]:
                    p = tf.add_paragraph()
                    p.text = bp
                    p.level = 0
            else:
                tf.text = slide_data.get('content', '')
    
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
