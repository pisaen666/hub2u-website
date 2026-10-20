---
name: Warm Neighborhood Market
colors:
  surface: '#fff8f6'
  surface-dim: '#e1d8d6'
  surface-bright: '#fff8f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf2f0'
  surface-container: '#f5ecea'
  surface-container-high: '#efe6e4'
  surface-container-highest: '#e9e1df'
  on-surface: '#1e1b1a'
  on-surface-variant: '#5a4138'
  inverse-surface: '#342f2e'
  inverse-on-surface: '#f8efed'
  outline: '#8e7166'
  outline-variant: '#e2bfb2'
  surface-tint: '#a73a00'
  primary: '#a33900'
  on-primary: '#ffffff'
  primary-container: '#cc4900'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb599'
  secondary: '#625e59'
  on-secondary: '#ffffff'
  secondary-container: '#e5ded8'
  on-secondary-container: '#66625d'
  tertiary: '#735733'
  on-tertiary: '#ffffff'
  tertiary-container: '#8e6f4a'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbce'
  primary-fixed-dim: '#ffb599'
  on-primary-fixed: '#370e00'
  on-primary-fixed-variant: '#7f2b00'
  secondary-fixed: '#e8e1db'
  secondary-fixed-dim: '#ccc5bf'
  on-secondary-fixed: '#1e1b17'
  on-secondary-fixed-variant: '#4a4641'
  tertiary-fixed: '#ffddb7'
  tertiary-fixed-dim: '#e6c095'
  on-tertiary-fixed: '#2a1800'
  on-tertiary-fixed-variant: '#5b4220'
  background: '#fff8f6'
  on-background: '#1e1b1a'
  surface-variant: '#e9e1df'
typography:
  display:
    fontFamily: Kanit
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 52px
  display-mobile:
    fontFamily: Kanit
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 42px
  headline-lg:
    fontFamily: Kanit
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 44px
  headline-lg-mobile:
    fontFamily: Kanit
    fontSize: 26px
    fontWeight: '600'
    lineHeight: 36px
  headline-md:
    fontFamily: Kanit
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 34px
  headline-sm:
    fontFamily: Kanit
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Prompt
    fontSize: 20px
    fontWeight: '400'
    lineHeight: 32px
  body-md:
    fontFamily: Prompt
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 30px
  label-lg:
    fontFamily: Prompt
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
  label-md:
    fontFamily: Prompt
    fontSize: 16px
    fontWeight: '500'
    lineHeight: 24px
  price-display:
    fontFamily: Kanit
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-desktop: 1.5rem
  margin: 1rem
  margin-desktop: 2.5rem
  space-xs: 0.5rem
  space-sm: 0.75rem
  space-md: 1.25rem
  space-lg: 2rem
  space-xl: 3rem
---

## Brand & Style

The design system embodies the warmth, sincerity, and communal reliability of a traditional Thai fresh market (ตลาดสดชุมชนเป็นมิตร อบอุ่น จริงใจ) adapted for digital accessibility. It intentionally rejects clinical tech-startup minimalism, high-frequency delivery aesthetics, and corporate neutrality. Instead, it creates an atmosphere reminiscent of visiting a familiar, multi-generational market stall where merchants know their regulars by name.

The visual style blends soft, tactile modernism with unpretentious hospitality. Key traits include:
- **Approachability & Tactility:** Generous touch targets, welcoming roundness, and organic warmth evoke tangible freshness rather than algorithmic logistics.
- **Elder-Inclusive Accessibility:** Sizing, contrast, and layout deliberately prioritize older demographics and non-tech-savvy community members through straightforward flows, prominent hierarchy, and frictionless readability.
- **Disciplined Warmth:** Color is applied deliberately. High-saturation tones are reserved for actions and essential indicators, while comfortable creams and soft whites carry the content without visual fatigue or chaotic over-stimulation.

## Colors

The palette draws directly from morning market sunlight, woven bamboo baskets, and honest harvest tones. 

### Color Application Rules
- **Primary (`#EA580C`):** Reserved exclusively for active primary Call-To-Action (CTA) buttons, critical status tags, interactive highlights, and high-priority badges. Never use as expansive full-bleed banner backgrounds or heavy structural fills.
- **Surface Hierarchy:**
  - Base canvas background: Warm Cream (`#FFF7ED`).
  - Card, modal, and elevated containers: Pure White (`#FFFFFF`).
  - Subtle interactive surfaces and pressed states: Warm Cream Tint (`#FEEBC8`).
- **Text & Contrast:**
  - Primary text: Dark Warm Charcoal (`#292524`) ensuring WCAG AAA accessibility across both cream and white backdrops.
  - Secondary supporting text: Muted Warm Stone (`#57534E`) for metadata, sub-labels, and item weights.
- **Borders & Dividers:** Low-contrast soft peach stone (`#FED7AA` and `#FEEBC8`) to define card boundaries without visual clutter.
- **Secondary Actions & Chat Access:** Neutral borders or soft stone fills (`#57534E` outline on white). Delivery app neon greens are strictly omitted to maintain neighborhood familiarity and avoid generic gig-economy cues.

## Typography

The typography stack pairs **Kanit** for prominent structural headings with **Prompt** for fluid, highly legible Thai and Latin body copy.

### Readability Guardrails
- **Minimum Base Size:** Standard body copy never drops below `18px` (`body-md`), preserving immediate readability for seniors under varied lighting conditions.
- **Thai Loop Anatomy & Spacing:** Prompt’s open counters and generous vertical proportions allow Thai diacritics (mai ek, mai tho, sara) to breathe without clipping or collision. The baseline line-height is locked at `1.6` for all narrative and list text.
- **Action Typography:** Primary button labels and category tags utilize `18px` (`label-lg`) with semi-bold weights (`600`) to guarantee legibility at glance speed.
- **Price Presentation:** Currency and unit weights are styled using `price-display` in Kanit bold to establish instant economic clarity.

## Layout & Spacing

The layout is built upon a responsive fluid grid optimized for mobile and tablet touch experiences while preserving a centered, max-width bounded view (`1200px`) on desktop viewports.

### Grid & Breakpoints
- **Mobile (< 768px):** 4-column fluid layout, `1rem` (16px) canvas margins, `1rem` (16px) column gutters. Elements emphasize single-column stacks or 2-column food product tiles.
- **Tablet (768px – 1024px):** 8-column fluid layout, `1.5rem` (24px) canvas margins, `1rem` gutters.
- **Desktop (> 1024px):** 12-column layout centered with max content width `1200px`, `2.5rem` (40px) outer margin, `1.5rem` (24px) gutters.

### Spacing Principles
- Standard vertical gap between distinct market stalls or categories is `space-xl` (48px) to prevent cognitive overload.
- Touch target clearance mandates at least `space-sm` (12px) separation between adjacent tappable items.
- Card padding remains generous at `space-md` (20px), preventing text and imagery from crowding component perimeters.

## Elevation & Depth

Visual depth utilizes soft, warm ambient shadows and tactile surface contrast rather than stark elevation planes or cold blurs.

### Surface Tiers
- **Canvas (Level 0):** Warm Cream (`#FFF7ED`). No shadow. Holds layout structures and structural dividers.
- **Resting Cards & Shelves (Level 1):** Solid White (`#FFFFFF`) framed by a subtle 1px border of `#FED7AA`. Enhanced by a warm ambient shadow:
  `box-shadow: 0px 4px 16px -2px rgba(41, 37, 36, 0.05), 0px 1px 3px 0px rgba(41, 37, 36, 0.03);`
- **Interactive Modals, Bottom Sheets & Floating Cart (Level 2):** Elevated pure white containers with an intensified, pillowed warm drop shadow:
  `box-shadow: 0px 12px 32px -4px rgba(41, 37, 36, 0.10), 0px 4px 8px -1px rgba(41, 37, 36, 0.04);`
- **Active State:** Tapping cards produces an inner resting feedback rather than harsh depression: gentle scaling (`0.99`) with subtle tone deepening to `#FEEBC8`.

## Shapes

The shape vocabulary uses friendly, organic rounds that soften the interface, avoiding clinical rectilinearity while maintaining sufficient structural discipline for clear organization.

- **Cards & Content Blocks:** Built with `rounded-lg` (16px) to emulate smooth display trays.
- **Input Fields & Stalls Chips:** Standardized at `rounded` (12px) to match finger pads.
- **Buttons & Counter Steppers:** Primary buttons and quantity steppers use `rounded-lg` (16px) or soft capsule styling where appropriate to maintain friendliness.
- **Market Stall Badges & Tags:** Styled with `rounded` (12px) with generous interior breathing room.

## Components

### Buttons
- **Primary CTA:** Minimum height `56px`. Background is `#EA580C`, text is pure white Kanit 18px semi-bold (`label-lg`), radius is 14px. Used for "Add to Basket" (ใส่ตะกร้า), "Confirm Order" (ยืนยันคำสั่งซื้อ), and primary checkout steps. Active state deepens to `#C2410C`.
- **Secondary Action & LINE Contact:** Minimum height `56px`. Surface is white `#FFFFFF` with a 2px solid `#FED7AA` or `#57534E` border, text is `#292524`. Provides high-contrast, anxiety-free secondary interactions.
- **Quantity Stepper (+/-):** Oversized `48px x 48px` circular or 12px rounded touch targets with large `20px` bold glyphs to ensure older patrons can effortlessly adjust quantities.

### Product Cards
- **Structure:** White `#FFFFFF` card, 1px border `#FED7AA`, radius 16px.
- **Image:** 1:1 ratio with subtle rounded top corners (14px). Food items are framed cleanly without artificial tinting.
- **Metadata:** Stall name in `#57534E` (16px), item title in `#292524` (Kanit 20px), followed by clear pricing formatted as `฿45 / กก.` with the number scaled to Kanit 24px bold.
- **Action:** Fixed-height quick-add button at bottom or oversized tap target.

### Input Fields
- **Container:** Height `56px`, background `#FFFFFF`, border 1.5px solid `#FED7AA`, radius 12px.
- **Typography:** Prompt 18px, placeholder text in `#78716C`.
- **States:** Focus replaces border with `#EA580C` accompanied by a soft 3px `#EA580C20` ambient halo.

### Selection Controls (Checkboxes & Radios)
- **Dimensions:** Sized to `28px x 28px` (larger than conventional 16-20px standards) to accommodate reduced motor precision.
- **Check State:** Solid `#EA580C` fill with high-contrast white checkmark icon. Unchecked displays a 2px `#FED7AA` outline on white.

### Chips & Category Filters
- **Default:** Height `44px`, background `#FFFFFF`, border 1px solid `#FED7AA`, text `#57534E` (Prompt 18px), radius 24px (pill-soft).
- **Active:** Background `#EA580C`, border 1px solid `#EA580C`, text `#FFFFFF`, font weight semi-bold.

### Floating Cart / Neighborhood Basket Bar
- Pinned to the viewport bottom with safe-area spacing. Full-width mobile bar elevated on White `#FFFFFF` with Level 2 warm shadow, presenting item count badge, large total sum in Kanit 24px, and an oversized `#EA580C` primary checkout trigger.