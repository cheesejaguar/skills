# Visualization Principles Reference

Quick-reference for building inline SVG charts and choosing typography in infographics.

---

## Chart Type Decision Tree

```
What are you showing?
|
+-- Comparison between categories?
|   +-- Few categories (2-8) -------> Horizontal Bar Chart
|   +-- Many categories (8+) -------> Top-N Horizontal Bars (truncate)
|   +-- Two items head-to-head -----> Side-by-side bars or comparison table
|
+-- Change over time?
|   +-- Continuous trend ------------> Line Chart
|   +-- Discrete periods ------------> Vertical Bar Chart
|   +-- Multiple series ------------> Multi-line Chart (max 4 lines)
|
+-- Part of a whole?
|   +-- 2-5 segments ---------------> Donut Chart
|   +-- 6+ segments ----------------> Stacked Horizontal Bar
|   +-- Simple ratio (X of Y) ------> Icon Grid / Pictogram
|
+-- Single key metric?
|   +-- One number ------------------> Big Number Callout
|   +-- Before/after ----------------> Two Big Numbers with arrow
|   +-- Percentage ------------------> Donut or progress bar
|
+-- Relationship between variables?
|   +-- Two numeric variables -------> Scatter Plot
|   +-- Categorical features -------> Comparison Table (CSS Grid)
|
+-- Distribution?
    +-- Single variable ------------> Histogram (vertical bars)
    +-- Comparing distributions ----> Side-by-side histograms
```

---

## SVG Chart Patterns

### Horizontal Bar Chart

Best for categorical comparison. Labels on the left, bars extending right.

```html
<svg viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg" aria-label="Bar chart comparing values">
  <!-- Label -->
  <text x="140" y="35" text-anchor="end" fill="var(--color-text)" font-size="14">Finland</text>
  <!-- Bar -->
  <rect x="150" y="20" width="400" height="24" rx="4" fill="var(--color-accent)"/>
  <!-- Value -->
  <text x="558" y="37" text-anchor="end" fill="#fff" font-size="13" font-weight="600">12.0 kg</text>

  <text x="140" y="75" text-anchor="end" fill="var(--color-text)" font-size="14">Norway</text>
  <rect x="150" y="60" width="360" height="24" rx="4" fill="var(--color-secondary)"/>
  <text x="518" y="77" text-anchor="end" fill="#fff" font-size="13" font-weight="600">9.9 kg</text>

  <text x="140" y="115" text-anchor="end" fill="var(--color-text)" font-size="14">Iceland</text>
  <rect x="150" y="100" width="340" height="24" rx="4" fill="var(--color-secondary)"/>
  <text x="498" y="117" text-anchor="end" fill="#fff" font-size="13" font-weight="600">9.0 kg</text>
</svg>
```

**Key rules:**
- Calculate bar width as `(value / maxValue) * maxBarWidth`
- Use `rx` for rounded corners (2-4px)
- Place value labels inside the bar when the bar is wide enough, outside when narrow
- Highlight the top item with `var(--color-accent)`, others with gray/muted — accent on the key finding only
- **Y-axis must start at zero** for bar charts — no exceptions
- Direct-label each bar; do not use a separate legend

### Donut Chart

Best for part-to-whole with 2-5 segments (hard max: 5 — more than 5, use stacked horizontal bars). Must sum to exactly 100%. Built with `stroke-dasharray` on circles.

```html
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-label="Donut chart">
  <!-- Background circle -->
  <circle cx="100" cy="100" r="70" fill="none" stroke="var(--color-divider)" stroke-width="28"/>

  <!-- Segment 1: 45% — dasharray = 0.45 * 2 * pi * 70 = 197.9 -->
  <circle cx="100" cy="100" r="70" fill="none"
    stroke="var(--color-accent)" stroke-width="28"
    stroke-dasharray="197.9 441.9" stroke-dashoffset="0"
    transform="rotate(-90 100 100)"/>

  <!-- Segment 2: 30% — dasharray = 0.30 * 439.8 = 131.9, offset = -197.9 -->
  <circle cx="100" cy="100" r="70" fill="none"
    stroke="var(--color-secondary)" stroke-width="28"
    stroke-dasharray="131.9 441.9" stroke-dashoffset="-197.9"
    transform="rotate(-90 100 100)"/>

  <!-- Center label -->
  <text x="100" y="95" text-anchor="middle" font-size="32" font-weight="700" fill="var(--color-text)">45%</text>
  <text x="100" y="115" text-anchor="middle" font-size="12" fill="var(--color-muted)">Market Share</text>
</svg>
```

**Key rules:**
- Circumference = `2 * Math.PI * radius`
- Each segment: `stroke-dasharray="segmentLength circumference"`
- Offset each subsequent segment by the cumulative length of previous segments (negative value)
- `transform="rotate(-90 cx cy)"` starts segments at 12 o'clock
- Place a summary stat in the center

### Line Chart

Best for trends over time. Built with `<polyline>` or `<path>`.

```html
<svg viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" aria-label="Line chart showing trend">
  <!-- Subtle gridlines -->
  <line x1="60" y1="30" x2="60" y2="210" stroke="var(--color-divider)" stroke-width="0.5"/>
  <line x1="60" y1="210" x2="570" y2="210" stroke="var(--color-divider)" stroke-width="0.5"/>

  <!-- Y-axis labels -->
  <text x="55" y="35" text-anchor="end" font-size="11" fill="var(--color-muted)">100</text>
  <text x="55" y="125" text-anchor="end" font-size="11" fill="var(--color-muted)">50</text>
  <text x="55" y="215" text-anchor="end" font-size="11" fill="var(--color-muted)">0</text>

  <!-- Area fill (optional, for visual weight) -->
  <polygon points="60,210 60,150 170,120 280,90 390,60 500,45 570,30 570,210"
    fill="var(--color-accent)" opacity="0.1"/>

  <!-- Line -->
  <polyline points="60,150 170,120 280,90 390,60 500,45 570,30"
    fill="none" stroke="var(--color-accent)" stroke-width="2.5"
    stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Data points -->
  <circle cx="60" cy="150" r="4" fill="var(--color-accent)"/>
  <circle cx="170" cy="120" r="4" fill="var(--color-accent)"/>
  <circle cx="280" cy="90" r="4" fill="var(--color-accent)"/>
  <circle cx="390" cy="60" r="4" fill="var(--color-accent)"/>
  <circle cx="500" cy="45" r="4" fill="var(--color-accent)"/>
  <circle cx="570" cy="30" r="4" fill="var(--color-accent)"/>

  <!-- X-axis labels -->
  <text x="60" y="230" text-anchor="middle" font-size="11" fill="var(--color-muted)">2020</text>
  <text x="170" y="230" text-anchor="middle" font-size="11" fill="var(--color-muted)">2021</text>
  <text x="280" y="230" text-anchor="middle" font-size="11" fill="var(--color-muted)">2022</text>
  <text x="390" y="230" text-anchor="middle" font-size="11" fill="var(--color-muted)">2023</text>
  <text x="500" y="230" text-anchor="middle" font-size="11" fill="var(--color-muted)">2024</text>
  <text x="570" y="230" text-anchor="middle" font-size="11" fill="var(--color-muted)">2025</text>
</svg>
```

**Key rules:**
- Map data values to Y coordinates: `y = chartBottom - (value / maxValue) * chartHeight`
- Map time indices to X coordinates: evenly distributed across chart width
- Use `stroke-linecap="round"` and `stroke-linejoin="round"` for smooth appearance
- Optional: add a semi-transparent polygon fill beneath the line for visual weight
- Add data point circles at each value for precision
- Max 4 lines on a single chart — use distinct colors with legend if multiple
- Line charts do NOT require a zero baseline (they encode via angle/slope, not length)
- **Half-frame:** Keep only left Y-axis and bottom X-axis lines; remove top and right borders
- Gridlines: `#EEEEEE`, `0.5-1px` stroke, major intervals only

### Big Number Callout

Best for hero statistics that anchor the narrative.

```html
<div class="big-number">
  <span class="stat-value">2.25B</span>
  <span class="stat-label">cups of coffee consumed daily worldwide</span>
</div>

<style>
.big-number {
  text-align: center;
  padding: 40px 20px;
}
.stat-value {
  display: block;
  font-family: var(--font-display);
  font-size: 96px;
  font-weight: 800;
  color: var(--color-accent);
  line-height: 1;
  letter-spacing: -2px;
}
.stat-label {
  display: block;
  font-family: var(--font-body);
  font-size: 18px;
  color: var(--color-muted);
  margin-top: 12px;
  max-width: 400px;
  margin-left: auto;
  margin-right: auto;
}
</style>
```

### Icon Grid (X out of Y)

Best for making proportions tangible ("7 out of 10 people...").

```html
<svg viewBox="0 0 300 60" xmlns="http://www.w3.org/2000/svg" aria-label="7 out of 10">
  <!-- Filled icons (7 active) -->
  <circle cx="20" cy="30" r="12" fill="var(--color-accent)"/>
  <circle cx="50" cy="30" r="12" fill="var(--color-accent)"/>
  <circle cx="80" cy="30" r="12" fill="var(--color-accent)"/>
  <circle cx="110" cy="30" r="12" fill="var(--color-accent)"/>
  <circle cx="140" cy="30" r="12" fill="var(--color-accent)"/>
  <circle cx="170" cy="30" r="12" fill="var(--color-accent)"/>
  <circle cx="200" cy="30" r="12" fill="var(--color-accent)"/>
  <!-- Empty icons (3 inactive) -->
  <circle cx="230" cy="30" r="12" fill="var(--color-divider)"/>
  <circle cx="260" cy="30" r="12" fill="var(--color-divider)"/>
  <circle cx="290" cy="30" r="12" fill="var(--color-divider)"/>
</svg>
```

**Key rules:**
- Use simple shapes (circles, person icons, relevant pictograms)
- Active items use accent color, inactive use muted/divider color
- Arrange in rows of 5 or 10 for easy counting
- For custom icons, use a simple `<path>` repeated via `<use>` with `xlink:href`

### Comparison Table

Best for feature-by-feature comparison. Built with CSS Grid, not `<table>`.

```html
<div class="comparison-grid">
  <div class="grid-header"></div>
  <div class="grid-header">Option A</div>
  <div class="grid-header">Option B</div>

  <div class="grid-label">Price</div>
  <div class="grid-cell">$9.99/mo</div>
  <div class="grid-cell highlight">$4.99/mo</div>

  <div class="grid-label">Storage</div>
  <div class="grid-cell highlight">100 GB</div>
  <div class="grid-cell">50 GB</div>
</div>

<style>
.comparison-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1px;
  background: var(--color-divider);
  border-radius: 8px;
  overflow: hidden;
}
.comparison-grid > div {
  background: var(--color-surface);
  padding: 16px;
  font-size: 15px;
}
.grid-header {
  font-weight: 700;
  background: var(--color-text);
  color: var(--color-surface);
  text-align: center;
}
.grid-label {
  font-weight: 600;
  color: var(--color-muted);
}
.grid-cell {
  text-align: center;
}
.grid-cell.highlight {
  color: var(--color-accent);
  font-weight: 700;
}
</style>
```

---

## Typography Scale

Modular scale (16px base, ~1.25 ratio) ensures visual hierarchy. Consistent sizing across all infographics:

| Element | Size | Weight | Font | Line Height |
|---|---|---|---|---|
| Hero stat numbers | 72-120px | 800 | Display | 1.0 |
| Infographic title | 48px | 800-900 | Display | 1.1 |
| Section headings | 31px | 700 | Display | 1.15 |
| Chart titles | 25px | 600 | Display | 1.2 |
| Bold labels | 20px | 600 | Display | 1.25 |
| Body text | 16-18px | 400 | Body | 1.5-1.6 |
| Chart labels | 13-14px | 500 | Body | 1.3 |
| Axis labels | 11-13px | 400 | Body | 1.3 |
| Source citations | 11-12px | 400 | Body | 1.4 |
| Micro (tick marks) | 10px min | 400 | Body | 1.0 |

### Line Length
Body text column width should be 480-560px (50-75 characters per line) inside the 900px infographic width. Wider lines reduce readability.

### Numeric Formatting
Always use `font-variant-numeric: tabular-nums` on all data numbers. This ensures digits are equal-width for perfect vertical alignment in charts, tables, and stacked stats. Add to your CSS:
```css
.stat-value, .chart-label, .table-cell, [data-value] {
  font-variant-numeric: tabular-nums;
}
```

Maintain consistent decimal precision across every chart — never mix "42%" and "38.5%" in the same visualization.

### Font Pairing Suggestions

Vary these across infographics — never repeat the same pairing consecutively:

- **Playfair Display** + Source Sans 3 — Classic editorial
- **Space Grotesk** + Inter — Modern tech
- **Fraunces** + Outfit — Warm and friendly
- **DM Serif Display** + DM Sans — Elegant and clean
- **Sora** + Nunito — Approachable and rounded
- **Bitter** + Raleway — Serious and structured
- **Archivo Black** + Work Sans — Bold and impactful
- **Cormorant Garamond** + Lato — Refined and literary
- **Oswald** + Merriweather Sans — Condensed headlines, readable body
- **Poppins** + Libre Baskerville — Contemporary meets traditional
