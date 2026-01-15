from pathlib import Path
import os
import shutil

def package_assets(deck_name: str, target_dir: Path) -> Path:
    """
    Bundles the output PPTX and its assets into a distribution folder.
    """
    from .deck_manager import get_deck_path
    deck_path = get_deck_path(deck_name)
    output_pptx = deck_path / "output" / f"{deck_name}.pptx"

    if not output_pptx.exists():
        raise FileNotFoundError(f"No generated deck found for '{deck_name}'")

    dist_path = target_dir / f"{deck_name}_dist"
    if dist_path.exists():
        shutil.rmtree(dist_path)
    os.makedirs(dist_path)

    # Copy PPTX
    shutil.copy2(output_pptx, dist_path / f"{deck_name}.pptx")

    # Copy Assets if they exist
    assets_src = deck_path / "assets"
    if assets_src.exists():
        shutil.copytree(assets_src, dist_path / "assets")

    return dist_path

def export_to_pdf(deck_name: str) -> Path:
    """
    Placeholder for PDF export.
    In a full production environment, this would use a tool like 'unoconv' or 'libreoffice'.
    """
    from .deck_manager import get_deck_path
    deck_path = get_deck_path(deck_name)
    output_pdf = deck_path / "output" / f"{deck_name}.pdf"

    # Simulate PDF generation for now
    with open(output_pdf, "w") as f:
        f.write("%PDF-1.4 (Placeholder for generated content)")

    return output_pdf
