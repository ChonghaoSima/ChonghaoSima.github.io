"""Generate placeholder thumbnail images for all publications."""
from PIL import Image, ImageDraw, ImageFont
import os

IMG_DIR = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(IMG_DIR, exist_ok=True)

W, H = 320, 220

# (filename, label, bg_color)
papers = [
    ("chi0", "χ₀", (100, 140, 180)),
    ("centaur", "Centaur", (160, 90, 90)),
    ("eta", "ETA", (90, 130, 100)),
    ("vlms_driving", "VLMs\nDriving", (130, 110, 160)),
    ("agibot", "AgiBot\nWorld", (170, 130, 70)),
    ("robot_manip", "Robot\nManip.", (80, 120, 140)),
    ("drivelm", "DriveLM", (180, 100, 60)),
    ("hintad", "Hint-AD", (100, 100, 150)),
    ("occnet", "Scene as\nOccupancy", (70, 130, 130)),
    ("uniad", "UniAD", (150, 80, 80)),
    ("bev_devils", "BEV\nDevils", (120, 120, 90)),
    ("leveraging", "Vision\nMulti-Modal", (90, 100, 140)),
    ("openlanev2", "OpenLane\nV2", (140, 100, 110)),
    ("sdf", "Sparse\nDense", (100, 130, 110)),
    ("openscene", "OpenScene", (130, 130, 80)),
    ("persformer", "PersFormer", (160, 110, 80)),
    ("bevformer", "BEVFormer", (80, 110, 150)),
    ("lshsmile", "LSH\nSMILE", (110, 90, 130)),
]

for fname, label, color in papers:
    img = Image.new("RGB", (W, H), color=color)
    draw = ImageDraw.Draw(img)

    # Lighter inner rectangle
    lighter = tuple(min(c + 40, 255) for c in color)
    draw.rounded_rectangle([10, 10, W - 10, H - 10], radius=12, fill=lighter)

    # Draw label text
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
    except Exception:
        font = ImageFont.load_default()

    lines = label.split("\n")
    total_h = len(lines) * 34
    y_start = (H - total_h) // 2
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        x = (W - tw) // 2
        y = y_start + i * 34
        # Shadow
        draw.text((x + 1, y + 1), line, fill=(0, 0, 0, 80), font=font)
        # Main text
        draw.text((x, y), line, fill=(255, 255, 255), font=font)

    path = os.path.join(IMG_DIR, f"{fname}.jpg")
    img.save(path, "JPEG", quality=85)
    print(f"  {path}")

print(f"\nGenerated {len(papers)} placeholder images.")
