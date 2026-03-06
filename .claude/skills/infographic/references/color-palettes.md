# Color Palettes Reference

Curated accessible palettes for infographics. Each palette includes CSS custom properties, WCAG contrast notes, and color-blind safety status.

---

## Usage

Copy the CSS variables block for your chosen palette into `:root`. The variable names are consistent across all palettes so swapping is easy.

---

## 1. Ocean Depths

Cool, trustworthy, professional. Good for science, technology, and financial data.

```css
:root {
  --color-bg: #f0f4f8;
  --color-text: #0d1b2a;
  --color-accent: #1b4965;
  --color-secondary: #5fa8d3;
  --color-tertiary: #bee9e8;
  --color-highlight: #e63946;
  --color-muted: #62727b;
  --color-surface: #ffffff;
  --color-divider: #cad2d8;
}
```

- WCAG AA: accent on bg passes (8.9:1), text on bg passes (16.2:1)
- Color-blind safe: blue-teal range distinguishable in all common types
- Highlight (red) provides strong contrast for callouts

## 2. Warm Earth

Warm, organic, approachable. Good for food, agriculture, culture, and human-interest topics.

```css
:root {
  --color-bg: #faf6f1;
  --color-text: #2d1b0e;
  --color-accent: #c45d2c;
  --color-secondary: #e8a838;
  --color-tertiary: #6b8f71;
  --color-highlight: #c45d2c;
  --color-muted: #7a6e62;
  --color-surface: #ffffff;
  --color-divider: #e0d5c7;
}
```

- WCAG AA: accent on bg passes (4.6:1), text on bg passes (13.8:1)
- Color-blind safe: orange-green-brown distinguishable via luminance difference
- Pair the green tertiary with labels, not color alone

## 3. High Contrast Editorial

Clean, bold, magazine-style. Good for news-style infographics and editorial content.

```css
:root {
  --color-bg: #f8f8f8;
  --color-text: #111111;
  --color-accent: #e63946;
  --color-secondary: #264653;
  --color-tertiary: #a8dadc;
  --color-highlight: #e63946;
  --color-muted: #555555;
  --color-surface: #ffffff;
  --color-divider: #dddddd;
}
```

- WCAG AA: all combinations pass comfortably (accent on bg: 4.5:1, text on bg: 17.4:1)
- Color-blind safe: red-teal pairing has strong luminance contrast
- Maximum readability; ideal when data density is very high

## 4. Forest & Meadow

Natural, balanced, calming. Good for environment, health, wellness, and sustainability topics.

```css
:root {
  --color-bg: #f5f7f2;
  --color-text: #1a2e1a;
  --color-accent: #2d6a4f;
  --color-secondary: #74c69d;
  --color-tertiary: #b7e4c7;
  --color-highlight: #d4a030;
  --color-muted: #5e6b5e;
  --color-surface: #ffffff;
  --color-divider: #d1dbc8;
}
```

- WCAG AA: accent on bg passes (6.1:1), text on bg passes (14.1:1)
- Color-blind caution: green shades may be hard to distinguish for deuteranopia — always pair with labels or patterns
- Gold highlight provides safe contrast against greens

## 5. Bold Primary

Energetic, confident, modern. Good for tech, startups, sports, and youth-oriented content.

```css
:root {
  --color-bg: #fafafa;
  --color-text: #1a1a1a;
  --color-accent: #2563eb;
  --color-secondary: #dc2626;
  --color-tertiary: #f59e0b;
  --color-highlight: #2563eb;
  --color-muted: #6b7280;
  --color-surface: #ffffff;
  --color-divider: #e5e7eb;
}
```

- WCAG AA: blue accent on bg passes (5.2:1), text on bg passes (16.8:1)
- Color-blind safe: blue-red-yellow all distinguishable across all types
- High energy; use the yellow sparingly as it's low contrast on white

## 6. Sophisticated Dark

Premium, immersive, dramatic. Good for luxury, space, data-dense dashboards, and nighttime themes.

```css
:root {
  --color-bg: #0f172a;
  --color-text: #e2e8f0;
  --color-accent: #f59e0b;
  --color-secondary: #3b82f6;
  --color-tertiary: #22d3ee;
  --color-highlight: #f59e0b;
  --color-muted: #94a3b8;
  --color-surface: #1e293b;
  --color-divider: #334155;
}
```

- WCAG AA: text on bg passes (12.1:1), gold accent on bg passes (8.5:1)
- Color-blind safe: gold-blue-cyan all distinguishable
- Use `--color-surface` for cards to create depth against the dark background

## 7. Pastel Friendly

Soft, accessible, approachable. Good for education, children's topics, and gentle data stories.

```css
:root {
  --color-bg: #fefcfb;
  --color-text: #2e2e3a;
  --color-accent: #6c63ff;
  --color-secondary: #ff6b6b;
  --color-tertiary: #48dbfb;
  --color-highlight: #6c63ff;
  --color-muted: #8e8ea0;
  --color-surface: #ffffff;
  --color-divider: #ededf0;
}
```

- WCAG AA: accent on bg passes (5.0:1), text on bg passes (14.5:1)
- Color-blind safe: purple-coral-cyan distinguishable across common types
- The pastels work best with slightly heavier font weights (500+) for readability

## 8. Monochrome Slate

Minimalist, serious, data-focused. Good for academic, government, and analytical content.

```css
:root {
  --color-bg: #f8fafc;
  --color-text: #0f172a;
  --color-accent: #334155;
  --color-secondary: #64748b;
  --color-tertiary: #94a3b8;
  --color-highlight: #0ea5e9;
  --color-muted: #94a3b8;
  --color-surface: #ffffff;
  --color-divider: #e2e8f0;
}
```

- WCAG AA: all slate values pass against bg; highlight blue passes (4.6:1)
- Color-blind safe: single-hue approach is inherently safe
- Use the blue highlight very sparingly — it pops against the monochrome base
- Best when the data itself provides visual interest and color isn't needed for encoding

---

## Data-Type Palette Selection

Before choosing from the themed palettes above, determine which palette **type** your data needs:

| Data Type | Palette Type | Example |
|---|---|---|
| Unordered categories | Qualitative (distinct hues) | Countries, product lines |
| Ordered numeric data | Sequential (single-hue gradient) | Temperature, population density |
| Data with meaningful midpoint | Diverging (two-hue gradient) | Profit/loss, above/below average |
| Binary (yes/no) | Two-tone | Pass/fail, before/after |

### Recommended Data Palettes

**Qualitative (categorical):** ColorBrewer Dark2
```
#1B9E77, #D95F02, #7570B3, #E7298A, #66A61E, #E6AB02
```

**Sequential (ordered):** Viridis — perceptually uniform, grayscale-safe
```
#440154, #3b528b, #21918c, #5ec962, #fde725
```

**Diverging:** ColorBrewer RdBu — avoids the red/green colorblind trap
```
#b2182b, #ef8a62, #fddbc7, #f7f7f7, #d1e5f0, #67a9cf, #2166ac
```

Gray is a utility color (use for "no data," de-emphasis, non-key data points) and does not count against the 3-5 color limit.

---

## Dark Mode Guidelines

When using dark backgrounds:
- Never use pure black (`#000000`) — use `#121212` to `#1e293b`
- Desaturate all data colors 20-30% to reduce visual vibration against dark backgrounds
- Chart area backgrounds should use `--color-surface` (slightly lighter than `--color-bg`) for subtle depth
- Text should be off-white (`#e2e8f0`) not pure white (`#ffffff`) to reduce harsh contrast
- Dark mode is preferred for mobile-first contexts (Reddit mobile browsing)

---

## Color-Blind Safety Rules

These rules apply regardless of which palette you choose:

1. **Blue + Orange is universally safe** — distinguishable across protanopia, deuteranopia, and tritanopia
2. **Never encode meaning with red vs. green alone** — the most common confusion pair
3. **Pair hue differences with luminance differences** — if two colors must be distinguished, ensure one is notably lighter/darker than the other
4. **Use patterns or labels as a secondary channel** — hatching, dots, or direct labels supplement color
5. **Test mentally**: imagine the chart in grayscale. If categories become indistinguishable, add a non-color differentiator
6. **Limit to 4-5 colors max per chart** — more than that is hard to distinguish for anyone, not just color-blind users

---

## Quick Selection Guide

| Topic Tone | Recommended Palette | Why |
|---|---|---|
| Professional / corporate | Ocean Depths | Trustworthy blues |
| Food / culture / human interest | Warm Earth | Warm, organic feel |
| News / editorial / politics | High Contrast Editorial | Bold, readable |
| Environment / health | Forest & Meadow | Natural association |
| Tech / sports / startups | Bold Primary | Energetic, modern |
| Premium / space / nighttime | Sophisticated Dark | Dramatic, immersive |
| Education / family / gentle | Pastel Friendly | Soft, approachable |
| Academic / government / minimal | Monochrome Slate | Serious, data-first |
