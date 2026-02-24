#!/usr/bin/env python3
"""
Composite Screenshots onto Gemini-Generated Slides

For slides that have ![right fit](image.png) references in Deckset markdown,
this script overlays the actual screenshot onto the right side of the
AI-generated Gemini slide image.

Layout:
  - Left 54%: Gemini AI-generated content (kept as-is)
  - Right 46%: Actual screenshot with dark background panel, rounded corners, shadow

Usage:
    python composite_screenshots.py "slides.md"
    python composite_screenshots.py "slides.md" --gemini-dir slides-gemini --dry-run
"""

import re
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFilter
except ImportError:
    print("Error: Pillow not installed. Run: pip install Pillow", file=sys.stderr)
    sys.exit(1)


def parse_slides_with_images(md_file: Path) -> dict:
    """
    Parse Deckset markdown to find slides with local image references.
    Returns dict: {slide_number (1-indexed): Path to image file}
    """
    base_dir = md_file.parent
    content = md_file.read_text(encoding='utf-8')

    # Remove frontmatter (slidenumbers: true, etc.)
    content = re.sub(r'^[a-z]+:\s*\S+\s*\n', '', content, flags=re.MULTILINE)

    raw_slides = content.split('---')

    slides_with_images = {}
    output_num = 0  # Sequential counter (only slides with speaker notes)

    for slide_content in raw_slides:
        slide_content = slide_content.strip()
        if not slide_content:
            continue

        # Only count slides with speaker notes (^ lines)
        notes_match = re.search(r'^\^\s*(.+?)$', slide_content, re.MULTILINE)
        if not notes_match:
            continue

        output_num += 1  # 1-indexed

        # Extract local image paths — ![alt](path)
        image_pattern = r'!\[[^\]]*\]\(([^)]+)\)'
        for match in re.finditer(image_pattern, slide_content):
            image_rel_path = match.group(1)
            image_path = base_dir / image_rel_path
            if image_path.exists():
                slides_with_images[output_num] = image_path
                break  # Use first valid image found per slide

    return slides_with_images


def composite_screenshot_onto_slide(
    slide_path: Path,
    screenshot_path: Path,
    output_path: Path,
    panel_start_ratio: float = 0.54,
    margin: int = 50,
    corner_radius: int = 16,
):
    """
    Composite a screenshot onto the right side of a slide image.

    Layout:
      - Dark semi-transparent overlay covers the right panel area
      - Screenshot placed centered in the right panel, with rounded corners + shadow
    """
    slide = Image.open(slide_path).convert('RGB')
    screenshot = Image.open(screenshot_path).convert('RGB')

    slide_w, slide_h = slide.size  # Typically 1920x1080

    # Define right panel area
    panel_x = int(slide_w * panel_start_ratio)
    panel_w = slide_w - panel_x - margin
    panel_h = slide_h - margin * 2
    panel_y = margin

    # Scale screenshot to fit in panel (maintain aspect ratio, leave inner padding)
    inner_pad = 20
    avail_w = panel_w - inner_pad * 2
    avail_h = panel_h - inner_pad * 2

    ss_ratio = screenshot.width / screenshot.height
    avail_ratio = avail_w / avail_h

    if ss_ratio > avail_ratio:
        new_w = avail_w
        new_h = int(new_w / ss_ratio)
    else:
        new_h = avail_h
        new_w = int(new_h * ss_ratio)

    screenshot_resized = screenshot.resize((new_w, new_h), Image.LANCZOS)

    # Center screenshot within panel
    x_pos = panel_x + inner_pad + (avail_w - new_w) // 2
    y_pos = panel_y + inner_pad + (avail_h - new_h) // 2

    # --- Compositing ---
    slide_rgba = slide.convert('RGBA')

    # 1. Dark semi-transparent panel background
    panel_overlay = Image.new('RGBA', (slide_w, slide_h), (0, 0, 0, 0))
    panel_draw = ImageDraw.Draw(panel_overlay)
    panel_draw.rounded_rectangle(
        [panel_x - 10, panel_y - 10, slide_w - margin + 10, panel_y + panel_h + 10],
        radius=20,
        fill=(0, 0, 30, 140)  # Dark navy, ~55% opacity
    )
    # Blur the panel slightly for smooth blend
    panel_overlay = panel_overlay.filter(ImageFilter.GaussianBlur(radius=8))
    slide_rgba = Image.alpha_composite(slide_rgba, panel_overlay)

    # 2. Drop shadow for screenshot
    shadow_offset = 8
    shadow_blur = 16
    shadow = Image.new('RGBA', (new_w + shadow_offset * 2 + shadow_blur,
                                 new_h + shadow_offset * 2 + shadow_blur), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle(
        [shadow_blur // 2, shadow_blur // 2,
         new_w + shadow_blur // 2 + shadow_offset,
         new_h + shadow_blur // 2 + shadow_offset],
        radius=corner_radius,
        fill=(0, 0, 0, 180)
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=shadow_blur // 2))

    shadow_x = x_pos - shadow_offset - shadow_blur // 2
    shadow_y = y_pos - shadow_offset - shadow_blur // 2
    slide_rgba.paste(shadow, (shadow_x, shadow_y), shadow)

    # 3. Screenshot with rounded corners
    ss_rgba = screenshot_resized.convert('RGBA')
    mask = Image.new('L', (new_w, new_h), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, new_w - 1, new_h - 1],
                                  radius=corner_radius, fill=255)
    ss_rgba.putalpha(mask)

    slide_rgba.paste(ss_rgba, (x_pos, y_pos), ss_rgba)

    # Save result
    result = slide_rgba.convert('RGB')
    result.save(output_path, 'JPEG', quality=95)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Composite actual screenshots onto Gemini-generated slide images'
    )
    parser.add_argument('markdown_file', type=Path,
                        help='Deckset markdown file (slides.md)')
    parser.add_argument('--gemini-dir', type=Path, default=Path('slides-gemini'),
                        help='Directory with Gemini-generated slide images (default: slides-gemini)')
    parser.add_argument('--output-dir', type=Path, default=None,
                        help='Output directory (default: same as gemini-dir, overwrites in place)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show which slides would be composited without doing it')

    args = parser.parse_args()

    if args.output_dir is None:
        args.output_dir = args.gemini_dir

    if not args.markdown_file.exists():
        print(f"Error: File not found: {args.markdown_file}", file=sys.stderr)
        sys.exit(1)

    print("🖼️  Composite Screenshots onto Gemini Slides")
    print("=" * 55)
    print(f"Markdown:   {args.markdown_file}")
    print(f"Gemini dir: {args.gemini_dir}")
    print(f"Output dir: {args.output_dir}")
    print()

    # Find slides with screenshot references
    slides_with_images = parse_slides_with_images(args.markdown_file)

    if not slides_with_images:
        print("No slides with local screenshot images found.")
        return

    print(f"Found {len(slides_with_images)} slides with screenshots:")
    for num, img_path in sorted(slides_with_images.items()):
        slide_path = args.gemini_dir / f"{num}.jpeg"
        exists = "✅" if slide_path.exists() else "❌ MISSING"
        print(f"  Slide {num:2d}: {img_path.name}  [{exists}]")

    if args.dry_run:
        print("\n(dry-run: no files written)")
        return

    print()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    success_count = 0
    skip_count = 0

    for slide_num, screenshot_path in sorted(slides_with_images.items()):
        slide_path = args.gemini_dir / f"{slide_num}.jpeg"
        output_path = args.output_dir / f"{slide_num}.jpeg"

        if not slide_path.exists():
            print(f"  ⚠️  Slide {slide_num}.jpeg not found — skipping")
            skip_count += 1
            continue

        print(f"  Compositing slide {slide_num:2d} ({screenshot_path.name})...", end=" ", flush=True)
        try:
            composite_screenshot_onto_slide(slide_path, screenshot_path, output_path)
            print("Done ✅")
            success_count += 1
        except Exception as e:
            print(f"FAILED ❌ ({e})")
            skip_count += 1

    print()
    print("=" * 55)
    print(f"Complete! Composited: {success_count}  Skipped: {skip_count}")
    print(f"Output: {args.output_dir}")


if __name__ == '__main__':
    main()
