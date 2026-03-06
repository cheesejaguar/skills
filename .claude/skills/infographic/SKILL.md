---
name: infographic
description: >
  Create beautiful, data-driven infographics as single-page HTML visualizations
  with automatic PNG screenshot capture and Reddit markdown source citations.
  Use this skill whenever the user mentions infographics, data visualization
  posters, visual reports, visual summaries, data storytelling, statistical
  graphics, chart posters, visual explainers, or wants to turn data/research
  into a shareable visual format — even if they don't explicitly say
  "infographic." Also use when users want to visualize survey results, create
  comparison charts, make visual fact sheets, or produce any tall-format
  data-rich visual output.
---

# Infographic Skill

## Overview

This skill produces three artifacts for every infographic:

1. **HTML** — A self-contained single-page visualization (900px fixed width, variable height) with embedded CSS, inline SVG charts, and Google Fonts. No external JS libraries.
2. **PNG** — A 2x retina screenshot captured via the bundled Playwright script.
3. **Reddit Markdown** — A standalone `.md` file with numbered source citations formatted for Reddit's editor.

The infographic should be visually distinctive and tell a clear narrative with 1-3 key messages (empirically backed limit — more than 3 splits attention and reduces recall). When the frontend-design skill is also available, apply its Design Thinking framework (Purpose, Tone, Constraints, Differentiation) and aesthetic guidelines adapted for the infographic's fixed-width, tall-format, static-capture context.

---

## Workflow

Follow these steps in order:

1. **Gather requirements** — Identify the topic, target audience, data sources, and desired tone. Ask clarifying questions if the scope is unclear. Write 1-3 specific claims the infographic must communicate as plain sentences before designing anything.

2. **Research and structure the data narrative** — Organize content into a narrative arc:
   - **Hook** — A surprising headline stat or question
   - **Context** — Background that frames the data
   - **Evidence** — Charts, comparisons, and supporting data
   - **Insight** — What the data reveals (the "so what?")
   - **Takeaway** — Actionable conclusion or memorable summary

3. **Choose aesthetic direction** — Select a color palette from `references/color-palettes.md` (3-5 colors maximum — empirically backed limit), pick a distinctive Google Fonts pairing (vary every time — never reuse the same pairing in consecutive infographics), and decide on visual style (editorial, playful, corporate, dark mode, etc.).

4. **Build the HTML** — Create a self-contained `.html` file following the HTML Specifications below. All charts are inline SVG. All styles are in a `<style>` block. All interactivity (if any) is in a `<script>` block.

5. **Capture the PNG** — Run the bundled screenshot script:
   ```
   python <skill-path>/scripts/capture_infographic.py <input.html> <output.png>
   ```

6. **Generate Reddit markdown citations** — Create a `.md` file with formatted source citations.

7. **Present all three files** — Show the user the HTML path, PNG path, and sources path. Offer to open the HTML in a browser.

---

## HTML Specifications

### Dimensions
- **Width:** 900px fixed (`max-width: 900px; margin: 0 auto;`)
- **Retina:** Rendered at 2x device scale (1800px PNG output width)
- **Height:** Variable — typically 2000-6000px, maximum ~8000px
- **Viewport meta:** `<meta name="viewport" content="width=900">`

### Self-Contained Requirements
- CSS in a single `<style>` block (no external stylesheets except Google Fonts)
- JavaScript in a single `<script>` block if needed (no external libraries — no D3, no Chart.js)
- Fonts via Google Fonts `<link>` tags in `<head>` (with system font fallbacks)
- All graphics as inline SVG elements or CSS-generated visuals
- No images via `<img>` tags — everything is SVG, CSS gradients, or CSS shapes

### Document Structure
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=900">
  <title>{Infographic Title}</title>
  <link href="https://fonts.googleapis.com/css2?family={Display+Font}&family={Body+Font}&display=swap" rel="stylesheet">
  <style>/* All styles here */</style>
</head>
<body>
  <!-- Hero / Header section -->
  <!-- Section dividers between major content blocks -->
  <!-- Data sections with inline SVG charts -->
  <!-- Conclusion / Takeaway -->
  <!-- Sources footer -->
  <script>/* Minimal JS if needed */</script>
</body>
</html>
```

### CSS Custom Properties
Define all colors at `:root` so the palette is easy to scan and modify:
```css
:root {
  --color-bg: #f8f6f2;
  --color-text: #1a1a2e;
  --color-accent: #e63946;
  --color-secondary: #457b9d;
  --color-tertiary: #a8dadc;
  --color-muted: #6b7280;
  --color-surface: #ffffff;
  --color-divider: #e5e7eb;
}
```

### Typography
- Always use two distinct Google Fonts: one display/heading font and one body/reading font (max 2 families; achieve hierarchy through weight/size, not font variety)
- Never reuse the same font pairing in consecutive infographics
- Use `font-variant-numeric: tabular-nums` on all data numbers for vertical alignment in charts and tables
- No prose paragraphs inside the infographic — use short phrases, bullet points, or sentence fragments only (lower parsing load)
- See `references/visualization-principles.md` for the typography scale and line heights

---

## Data Visualization Principles

### Narrative Structure
Every infographic tells a story with 1-3 key messages. The title should state the **conclusion**, not just the topic (e.g., "Nordic Countries Drink 3x More Coffee Than the US" not "Global Coffee Consumption"). Structure:
1. **Hook** — Open with a surprising statistic, bold claim, or provocative question rendered as a hero element (large number, bold typography)
2. **Context** — Provide background: timeline, scope, definitions. Use simple charts or icon grids.
3. **Evidence** — Present the core data. Use 2-4 chart types maximum per infographic. Let the data speak.
4. **Insight** — Highlight what the data reveals. Call out key findings with big numbers or highlight boxes.
5. **Takeaway** — End with a clear conclusion, call to action, or memorable summary statement.

**5-second test:** A reader should be able to extract the core message by scanning the hero and section headings in under 5 seconds. If not, reduce complexity.

### Perceptual Encoding Hierarchy (Cleveland & McGill)
When choosing how to encode data, prefer encodings higher on this empirically tested accuracy ranking:
1. **Position along a common scale** (bar chart, dot plot) — most accurate
2. **Length** (bar chart)
3. **Angle / slope** (line chart steepness)
4. **Area** (bubble chart, treemap) — much less accurate
5. **Color saturation** — least accurate

**Implication:** Default to bar charts over pie/donut charts for comparison tasks. Bar charts use position/length (rank 1-2); pie charts use angle/area (rank 3-4).

### Chart Type Selection
Match the chart type to the data relationship:

| Data Relationship | Recommended Chart | SVG Elements |
|---|---|---|
| Comparison (categorical) | Horizontal bar chart | `<rect>` + `<text>` |
| Trend over time | Line chart | `<polyline>` or `<path>` |
| Part-to-whole (2-5 categories) | Donut chart | `<circle>` with `stroke-dasharray` |
| Part-to-whole (6+ categories) | Stacked horizontal bar | `<rect>` elements |
| Correlation | Scatter plot | `<circle>` elements |
| Single key metric | Big number callout | Styled `<text>` or HTML |
| Proportion (X of Y) | Icon grid / pictogram | Repeated `<path>` icons |
| Feature comparison | Comparison table | CSS Grid layout |
| Distribution | Histogram / bar chart | `<rect>` elements |
| Ranking | Ordered horizontal bars | `<rect>` sorted by value |
| Flow / funnel / budget | Sankey-style flow | `<path>` with curves |
| Daily patterns over time | Calendar heat map | `<rect>` grid |

**Hard rules:**
- Bar/column chart Y-axes **must start at zero** — no exceptions for absolute values
- Donut/pie charts must sum to exactly 100% with a maximum of 5 segments
- Line charts do NOT require zero baselines (they encode via angle, not length)
- Never use 3D charts, radar charts, or bar chart races

### Data-Ink Ratio (Tufte)
Maximize the share of ink used to present data. Clutter negates the ~19% cognitive load advantage that clean visualizations have over equivalent text.
- No 3D effects, gradient fills on bars, or decorative chart borders
- **Half-frame technique:** Keep only the left Y-axis and bottom X-axis — remove top and right borders
- Gridlines: subtle `#EEEEEE` at `0.5-1px`, major intervals only (e.g., 0/25/50/75/100)
- **Direct-label data points instead of using legends** — legends force eye travel and increase cognitive load (Tufte). Place the label on or adjacent to the data element.
- Remove axes entirely when direct labels make them redundant
- Use accent color only on the key data point; use gray/muted for everything else

### Pre-Attentive Attributes
Use these visual properties strategically to draw attention:
- **Color** — Use accent color sparingly to highlight the most important data point
- **Size** — Make key numbers 3-6x larger than body text
- **Position** — Place the most important information at the top and in the visual center
- **Contrast** — Use high contrast for key data, low contrast for supporting context

### Gestalt Principles
- **Proximity** — Group related data elements close together
- **Similarity** — Use consistent color/shape for items in the same category
- **Enclosure** — Use subtle background fills to group related sections
- **Connection** — Use lines or arrows to show relationships between elements

### Accessibility
- All color combinations must meet WCAG AA contrast ratio (4.5:1 for text, 3:1 for large text/graphical elements)
- Never rely on color alone to convey meaning — pair with labels, patterns, or icons
- Use color-blind safe palettes (see `references/color-palettes.md`) — red-green opposition affects ~8% of men
- All axis labels must be horizontal — diagonal labels are universally criticized as unreadable
- Include `aria-label` on SVG chart containers
- Use semantic HTML where possible (`<section>`, `<header>`, `<footer>`)
- Maintain consistent decimal precision across all charts (never mix "42%" and "38.5%")

### SVG Chart Construction
All charts are built with inline SVG elements — no external charting libraries:
- Bars: `<rect>` with `<text>` labels, rounded ends (`rx="2"` to `rx="4"`)
- Donuts: `<circle>` with `stroke-dasharray` and `stroke-dashoffset`
- Lines: `<polyline>` or `<path>` with `d` attribute
- Points: `<circle>` elements
- Text labels: `<text>` with proper `text-anchor` and `dominant-baseline`
- Declare all fonts in the HTML `<head>`, not only in SVG-embedded stylesheets (ensures Playwright loads them)
- Reference `references/visualization-principles.md` for detailed SVG patterns and code snippets

### Mandatory Source Attribution
Every infographic **must** include source attribution — this is the #1 criticism when missing (per r/dataisbeautiful analysis). The infographic's HTML footer must include:
- Data source names with dates/time periods
- Tool attribution: "Created with Claude"
- These same sources appear in the standalone Reddit markdown file

### Anti-Patterns (Never Do These)
| Anti-Pattern | Why It Fails |
|---|---|
| Pie chart with 6+ slices | Angle/area judgment is inaccurate; use horizontal bars |
| 3D effects on any chart | Distorts proportions, adds chartjunk |
| Legend separated from data | Forces eye travel; use direct labels instead |
| More than 5 colors in a chart | Degrades differentiation, overloads working memory |
| Prose paragraphs in infographic | High parsing load; use short phrases/bullets |
| Gradient/texture fills on bars | Visual noise without data encoding; use flat fills |
| Truncated Y-axis on bar chart | Distorts magnitude of differences |
| Diagonal axis labels | Universally criticized as unreadable; always horizontal |
| Red vs. green as opposites | Fails for ~8% of male viewers; use blue-orange |
| Rainbow/jet color maps | Perceptually non-uniform; use Viridis or single-hue sequential |
| Decorative color (no data encoding) | "What does the color mean?" — if it doesn't encode data, remove it |
| Missing source attribution | Most common criticism on data viz communities |

---

## Aesthetic Direction

### Design Philosophy
Each infographic should feel crafted and intentional — not like a generic template. Vary the aesthetic across infographics. Consider the topic's tone: a public health infographic feels different from a tech industry comparison or a sports statistics poster.

### Backgrounds
- Subtle textures: light paper-like noise via SVG filters, soft gradients
- Never use plain flat white — add warmth with off-whites (`#f8f6f2`, `#fafaf7`) or subtle gradients
- Dark mode infographics: use rich dark backgrounds (`#0f172a`, `#1a1a2e`) with light text
- SVG filter for paper texture:
```svg
<filter id="noise"><feTurbulence baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/><feBlend in="SourceGraphic" mode="multiply" result="blend"/></filter>
```

### Color
- **3-5 colors maximum per infographic** (Murray et al., 2017) — more degrades categorical differentiation
- Every color must encode data or serve a structural purpose — no decorative color
- Choose one dominant color + 2-3 accents from `references/color-palettes.md`
- Use the dominant color for headings and key data; accents for chart highlights
- Reserve one high-contrast accent for the single most important data point
- Use gray/muted for all non-key data points — accent color on the key finding only
- **Chart area backgrounds must be flat neutral** — never place gradients behind charts
- **Dark mode:** desaturate all data colors 20-30% on dark backgrounds; never use pure black (`#000000`) — use `#121212` to `#1a1a2e`

### Section Dividers
Separators between major sections, from most to least subtle (prefer subtlety):
1. **Whitespace alone** (60-80px) — most sophisticated, often sufficient
2. **Short accent line** — 3-4px tall, 40-60px wide, accent color, centered
3. **Alternating section backgrounds** — white / very light gray bands
4. **SVG wave shapes or curves** — use sparingly, max 1-2 per infographic
5. **Color band transitions** — gradient from one section color to the next
6. **Angled dividers** via CSS `clip-path`

Avoid plain `<hr>` lines. Geometric SVG dividers (waves, chevrons) add visual interest but overuse feels gimmicky.

### Animations (CSS)
CSS animations enhance the HTML viewing experience. The screenshot script uses `animations="disabled"` which deterministically fast-forwards all CSS animations to their end state — no timing issues.
- Use `animation-fill-mode: both` so the final state is always visible
- Entrance animations: fade-in, slide-up, scale-in
- Stagger animations with `animation-delay` for sequential reveals
- Keep durations short (300-600ms)
- Do NOT use SVG SMIL animations (`<animate>`, `<animateTransform>`) — they are not affected by Playwright's animation disabling

### White Space
- Maintain 60-80px vertical padding between major sections
- Use generous internal padding in cards and data containers (24-40px)
- Let the infographic breathe — density comes from data richness, not visual cramming

### Icons
- Use simple inline SVG icons for visual interest and quick comprehension
- Pick one icon style and use it consistently: line, solid, or filled — never mixed
- Keep a consistent stroke width across all icons in one infographic
- Sizing: section headers 32-48px, inline 20-24px, decorative background 120-200px at 10-20% opacity
- Icons supplement text — they never replace labels
- Place icons at section headers, stat callouts, and list bullets — not next to every text block

---

## Screenshot Capture

The bundled Python script handles PNG generation:

```bash
python <skill-path>/scripts/capture_infographic.py <input.html> <output.png>
```

### Arguments
- `input.html` — Path to the HTML infographic file (required)
- `output.png` — Path for the PNG output (optional, defaults to input name with `.png`)
- `--width` — Viewport width in pixels (default: 900)
- `--scale` — Device scale factor (default: 2 for retina)

### What It Does
1. Checks that Playwright is installed; prints install instructions if not
2. Launches headless Chromium with `--force-color-profile=srgb` (prevents washed-out colors) and `--font-render-hinting=none` (consistent text rendering)
3. Sets a real Chrome User-Agent so Google Fonts serves WOFF2 with full Unicode subsets
4. Navigates to `file://` URL with `wait_until="networkidle"`
5. Waits for `document.fonts.ready` to ensure Google Fonts have loaded
6. Measures content height, resizes viewport to exact content dimensions (avoids the `full_page=True` 1px resize bug)
7. Captures with `scale="device"` (required for retina output) and `animations="disabled"` (CSS animations fast-forwarded to end state)
8. Prints the output path and image dimensions

### Installation (if needed)
```bash
pip install playwright && playwright install chromium
```

---

## Reddit Markdown Citations

Generate a standalone `.md` file with source citations formatted for Reddit:

### Format
```markdown
**Sources:**

1. [Source Title](https://example.com/article) - Brief description of what data was used
2. [Another Source](https://example.com/data) - Description of the dataset or finding

---

*Infographic created with Claude*
```

### Rules
- Use double newlines between items for Reddit paragraph spacing
- Bold the "Sources:" header with `**Sources:**`
- Number each source with `1.`, `2.`, etc.
- Each source: `[Display Title](URL) - one-line description`
- End with a horizontal rule `---` and italic footer `*Infographic created with Claude*`
- The same sources must appear in both the infographic's HTML footer AND this standalone file
- If a source has no URL (e.g., "Bureau of Labor Statistics data"), format as plain text without a link

---

## Output Files

All output files use a consistent naming convention with a kebab-case topic slug:

- `infographic-{topic-slug}.html` — The self-contained HTML infographic
- `infographic-{topic-slug}.png` — The 2x retina PNG screenshot
- `infographic-{topic-slug}-sources.md` — Reddit markdown citations

Example: For a topic of "Global Coffee Consumption", files would be:
- `infographic-global-coffee-consumption.html`
- `infographic-global-coffee-consumption.png`
- `infographic-global-coffee-consumption-sources.md`

---

## Example Walkthrough

**User prompt:** "Create an infographic about global coffee consumption"

1. **Gather requirements** — Topic: global coffee consumption. Audience: general/Reddit. Tone: warm, editorial.

2. **Research** — Find data on top producing/consuming countries, per-capita consumption, market size, trends.

3. **Aesthetic** — Choose "Warm Earth" palette, fonts: Playfair Display + Source Sans 3. Warm background with coffee-toned accents.

4. **Build HTML** — Structure:
   - Hero: "The world drinks 2.25 billion cups of coffee every day" (big number)
   - Context: Brief history, global market size
   - Evidence: Horizontal bar chart of top 10 consuming countries, donut chart of production by region, line chart of consumption trend over 20 years
   - Insight: "Nordic countries drink 3x more coffee per capita than the US"
   - Takeaway: Summary stat + sources footer

5. **Capture PNG:**
   ```bash
   python .claude/skills/infographic/scripts/capture_infographic.py infographic-global-coffee-consumption.html infographic-global-coffee-consumption.png
   ```

6. **Generate sources.md** with Reddit formatting

7. **Present** all three files to the user
