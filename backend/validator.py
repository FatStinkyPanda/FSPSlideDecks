from pathlib import Path

from pptx import Presentation

def validate_pptx(file_path: Path) -> dict:
    """
    Performs quality checks on a generated PPTX file.
    Returns a result dict with success status and any issues found.
    """
    results = {
        "valid": True,
        "issues": [],
        "slide_count": 0
    }

    if not file_path.exists():
        results["valid"] = False
        results["issues"].append("File does not exist.")
        return results

    try:
        prs = Presentation(file_path)
        results["slide_count"] = len(prs.slides)

        if results["slide_count"] == 0:
            results["valid"] = False
            results["issues"].append("Presentation has no slides.")

        for i, slide in enumerate(prs.slides):
            if not slide.shapes.title or not slide.shapes.title.text.strip():
                results["issues"].append(f"Slide {i+1} has an empty or missing title.")
                # We won't mark it invalid, just record the issue

    except Exception as e:
        results["valid"] = False
        results["issues"].append(f"Failed to parse PPTX file: {e}")

    return results
