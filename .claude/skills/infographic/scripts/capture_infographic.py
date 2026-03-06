#!/usr/bin/env python3
"""Capture a full-page PNG screenshot of an HTML infographic using Playwright."""

import argparse
import sys
from pathlib import Path

# Chromium launch args for consistent, high-quality rendering
LAUNCH_ARGS = [
    # Lock output to sRGB — prevents washed-out colors on non-sRGB OS profiles (e.g. macOS Display P3)
    "--force-color-profile=srgb",
    # Disable LCD sub-pixel hinting — produces consistent grayscale antialiasing across environments
    "--font-render-hinting=none",
    # Prevent shared memory exhaustion in Docker/Linux containers
    "--disable-dev-shm-usage",
]

# Real Chrome UA ensures Google Fonts serves WOFF2 with full Unicode subsets
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


def check_playwright():
    """Check if Playwright is installed and return helpful error if not."""
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
        return True
    except ImportError:
        print("Error: Playwright is not installed.", file=sys.stderr)
        print("Install it with:", file=sys.stderr)
        print("  pip install playwright && playwright install chromium", file=sys.stderr)
        return False


def capture(input_html: str, output_png: str, width: int = 900, scale: int = 2):
    """Capture a full-page screenshot of the given HTML file."""
    from playwright.sync_api import sync_playwright

    input_path = Path(input_html).resolve()
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    output_path = Path(output_png).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    file_url = input_path.as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=LAUNCH_ARGS)
        context = browser.new_context(
            viewport={"width": width, "height": 800},
            device_scale_factor=scale,
            user_agent=USER_AGENT,
        )
        page = context.new_page()

        # Navigate and wait for all network requests (including font files) to settle
        page.goto(file_url, wait_until="networkidle", timeout=30000)

        # Wait for all web fonts to finish loading via the Font Loading API
        page.evaluate("() => document.fonts.ready")

        # Measure actual content height and resize viewport to match —
        # avoids the full_page=True internal 1px resize bug (playwright#30149)
        # that can break vh units, sticky elements, and CSS Grid layouts
        content_height = page.evaluate(
            "() => Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)"
        )
        page.set_viewport_size({"width": width, "height": content_height})

        # Brief pause for layout reflow after viewport resize
        page.wait_for_timeout(100)

        # Capture with animations="disabled" — CSS animations are fast-forwarded
        # to their end state deterministically (no timing guesswork).
        # scale="device" is REQUIRED — without it, deviceScaleFactor is silently
        # ignored and the output renders at 1x.
        page.screenshot(
            path=str(output_path),
            type="png",
            scale="device",
            animations="disabled",
            clip={"x": 0, "y": 0, "width": width, "height": content_height},
        )

        actual_width = width * scale
        actual_height = content_height * scale

        context.close()
        browser.close()

    print(f"Screenshot saved: {output_path}")
    print(f"Dimensions: {actual_width}x{actual_height}px (at {scale}x scale)")


def main():
    parser = argparse.ArgumentParser(
        description="Capture a full-page PNG screenshot of an HTML infographic."
    )
    parser.add_argument("input", help="Path to the HTML infographic file")
    parser.add_argument(
        "output",
        nargs="?",
        default=None,
        help="Path for the PNG output (default: input name with .png extension)",
    )
    parser.add_argument(
        "--width", type=int, default=900, help="Viewport width in pixels (default: 900)"
    )
    parser.add_argument(
        "--scale", type=int, default=2, help="Device scale factor (default: 2 for retina)"
    )

    args = parser.parse_args()

    if not check_playwright():
        sys.exit(1)

    output = args.output
    if output is None:
        output = str(Path(args.input).with_suffix(".png"))

    capture(args.input, output, args.width, args.scale)


if __name__ == "__main__":
    main()
