from pathlib import Path
from PyPDF2 import PdfReader
from PIL import Image

def pdf_to_text_file(src: str, dest: str) -> None:
    reader = PdfReader(src)
    text = "\n".join(p.extract_text() or "" for p in reader.pages)
    Path(dest).write_text(text, encoding="utf-8")

def image_to_png_file(src: str, dest: str) -> None:
    img = Image.open(src)
    rgb = img.convert("RGBA")
    rgb.save(dest, format="PNG")