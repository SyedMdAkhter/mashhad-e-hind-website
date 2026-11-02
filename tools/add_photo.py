"""Add a photo to the Home page gallery.

    python3 tools/add_photo.py path/to/photo.jpg my-photo-id "English description"

Writes assets/gallery/<id>-600.jpg (grid) and <id>-1600.jpg (full view), then
prints the GALLERY entry to paste at the top of the list in tools/generate.py.
Add "hi", "pa" and "ur" descriptions to the entry when they are available.
Needs Pillow (python3 -m pip install Pillow).
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent


def main():
    src, photo_id, caption = sys.argv[1], sys.argv[2], sys.argv[3]
    out = ROOT / "assets" / "gallery"
    out.mkdir(parents=True, exist_ok=True)
    img = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    sizes = {}
    for width in (600, 1600):
        copy = img.copy()
        copy.thumbnail((width, width * 2))
        copy.save(out / f"{photo_id}-{width}.jpg", "JPEG", quality=82, optimize=True, progressive=True)
        sizes[width] = copy.size
    print(f'    {{"id": "{photo_id}", "size": {sizes[600]}, "en": "{caption}"}},')


if __name__ == "__main__":
    main()
