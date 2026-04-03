# Visual Preview Guide - MediaMass Modern

## 🎨 Color Scheme

```
PRIMARY GRADIENT
┌─────────────────────────────────────┐
│  Violet (#8b5cf6) → Pink (#ec4899)  │
└─────────────────────────────────────┘

BACKGROUND GRADIENT
┌─────────────────────────────────────┐
│  Slate-950 → Purple-950 → Slate-950 │
│  (Deep dark with purple tint)       │
└─────────────────────────────────────┘

TEXT COLORS
• Primary: White (#ffffff)
• Secondary: Gray-300 (#d1d5db)
• Tertiary: Gray-400 (#9ca3af)
• Accents: Green-400 (#4ade80)
```

---

## 📐 Layout Structure

```
┌─────────────────────────────────────────────┐
│  NAV (Fixed)                          ☰     │ ← Glassmorphism
├─────────────────────────────────────────────┤
│                                             │
│        ○  ○  ○  (Floating Orbs)            │
│                                             │
│     Mass Video Posting                      │
│        At Scale                             │ ← Hero Section
│                                             │
│  [Get Started] [View Packages]             │
│                                             │
├─────────────────────────────────────────────┤
│                                             │
│   ┌───────┐  ┌───────┐  ┌───────┐         │
│   │ 250K+ │  │  2+   │  │ 24/7  │         │ ← Stats
│   └───────┘  └───────┘  └───────┘         │
│                                             │
├─────────────────────────────────────────────┤
│                                             │
│   ┌────┐ ┌────┐ ┌────┐                    │
│   │Icon│ │Icon│ │Icon│                    │ ← Features
│   └────┘ └────┘ └────┘                    │
│   ┌────┐ ┌────┐ ┌────┐                    │
│   │Icon│ │Icon│ │Icon│                    │
│   └────┘ └────┘ └────┘                    │
│                                             │
├─────────────────────────────────────────────┤
│                                             │
│   ┌────────┐ ┌────────┐ ┌────────┐        │
│   │Starter │ │  Pro   │ │Enterprise│       │ ← Packages
│   │  $99   │ │ $299   │ │ Custom  │       │
│   └────────┘ └────────┘ └────────┘        │
│                                             │
├─────────────────────────────────────────────┤
│  MediaMass    Links    © 2026               │ ← Footer
└─────────────────────────────────────────────┘
```

---

## 🎬 Animation Sequence

### Page Load (0-2s)
```
t=0s:   Page loads, orbs start floating
t=0.1s: Hero title fades in from bottom
t=0.3s: Badge fades in
t=0.5s: Subheadline appears
t=0.7s: CTA buttons slide in
```

### Scroll Animation Timeline
```
Scroll: 0% → Hero visible
        ↓
Scroll: 20% → Stats cards slide up (counter starts)
        ↓
Scroll: 40% → Feature cards fade in (staggered)
        ↓
Scroll: 60% → Package cards appear
        ↓
Scroll: 100% → Footer
```

---

## 📱 Responsive Breakpoints

### Mobile (< 768px)
```
┌─────────────┐
│    NAV  ☰   │
├─────────────┤
│   Hero      │
│  (Centered) │
│             │
│ [CTA Full]  │
│ [CTA Full]  │
├─────────────┤
│  ┌───────┐  │
│  │ Stat  │  │
│  └───────┘  │
│  ┌───────┐  │
│  │ Stat  │  │
│  └───────┘  │
└─────────────┘
```

### Tablet (768px - 1024px)
```
┌─────────────────────────┐
│    NAV           Links  │
├─────────────────────────┤
│       Hero              │
│    (2 columns)          │
│   [CTA 1] [CTA 2]       │
├─────────────────────────┤
│  ┌──────┐  ┌──────┐    │
│  │ Stat │  │ Stat │    │
│  └──────┘  └──────┘    │
└─────────────────────────┘
```

### Desktop (> 1024px)
```
┌─────────────────────────────────────────┐
│  NAV         Links       [CTA]          │
├─────────────────────────────────────────┤
│          Hero (Full Width)              │
│      [CTA 1]    [CTA 2]                 │
├─────────────────────────────────────────┤
│  ┌─────┐  ┌─────┐  ┌─────┐             │
│  │Stat1│  │Stat2│  │Stat3│             │
│  └─────┘  └─────┘  └─────┘             │
└─────────────────────────────────────────┘
```

---

## 🎯 Interactive Elements

### Hover States

**Buttons:**
```
Normal:  [────────────]
         ↓
Hover:   [░░░░░░░░░░░░] ← Glow + Scale 105%
```

**Cards (Glass):**
```
Normal:  ┌─────────────┐
         │   Content   │
         └─────────────┘
         ↓
Hover:   ┌═════════════┐ ← Lift + Border Glow
         │   Content   │
         └═════════════┘
```

**Links:**
```
Normal:  Features
         ↓
Hover:   Features
         ━━━━━━━━ ← Gradient underline
```

### Click Effects

**Button Ripple:**
```
Click Position: ●
         ↓
Expand:  ◉
         ↓
Fade:    ○ (disappears)
```

---

## 🌈 Visual Effects

### Glassmorphism
```
Background: rgba(255, 255, 255, 0.03)
Border: rgba(255, 255, 255, 0.1)
Blur: 10px backdrop-filter
Shadow: 0 8px 32px rgba(0, 0, 0, 0.1)
```

### Gradient Examples
```
Text:    MediaMass
         ↓
         𝗩𝗜𝗗𝗜𝗠𝗔𝗦𝗦 (Violet → Pink)

Button:  [▓▓▓▓▓▓▓▓▓▓]
         Violet → Pink gradient + hover glow

Stats:   250K+ (Gradient text)
```

### Floating Orbs
```
   ○         Large orb (500px, Violet-Pink)
      ○      Medium orb (400px, Pink-Violet)
        ○    Small orb (300px, Purple-Pink)

Animation: Slow float (20s loop)
Blur: 80px (creates soft glow)
Opacity: 15% (subtle background effect)
```

---

## 🎨 Component Examples

### Hero Badge
```
┌────────────────────────────┐
│ ● 24/7 Distribution Active │ ← Glass, Green dot pulses
└────────────────────────────┘
```

### Stat Card
```
┌─────────────────────────┐
│                         │
│       250K+             │ ← Large gradient number
│   Videos Per Day        │ ← Gray-300 text
│ Maximum Distribution... │ ← Gray-500 subtext
│                         │
└─────────────────────────┘
Hover: Lifts up, glows
```

### Feature Card
```
┌─────────────────────────┐
│  ┌────┐                 │
│  │ ⚡ │ Lightning Fast  │ ← Icon + Title
│  └────┘                 │
│  Upload and distribute  │
│  thousands of videos... │ ← Description
└─────────────────────────┘
```

### Package Card (Pro - Featured)
```
┌─────────────────────────┐
│     🌟 POPULAR          │ ← Badge
├─────────────────────────┤
│  PRO                    │
│  $299/mo                │
│                         │
│  ✓ Up to 50K videos     │
│  ✓ All platforms        │
│  ✓ Advanced analytics   │
│  ✓ Priority support     │
│  ✓ API access           │
│                         │
│  [   Get Started   ]    │ ← Gradient button
└─────────────────────────┘
Border: Violet glow, Scale 105%
```

---

## 📊 Typography Scale

```
Logo:       24px    Poppins Bold    Gradient
H1 (Hero):  64-96px Poppins Black   White/Gradient
H2:         40-48px Poppins Bold    White/Gradient
H3 (Card):  20px    Poppins Semibold White
Body:       16-18px Inter Regular    Gray-300
Small:      14px    Inter Regular    Gray-400
Tiny:       12px    Inter Regular    Gray-500
```

---

## 🎭 Animation Timings

```
Fast:    0.15s - 0.3s   (Hover effects)
Medium:  0.5s - 0.8s    (Slide-in, fade)
Slow:    1s - 2s        (Hero entrance)
Ultra:   20s            (Floating orbs)

Easing:
- ease-out (most animations)
- ease-in-out (floating orbs)
- cubic-bezier() for custom
```

---

## 🔮 Special Effects

### Parallax Layers
```
Layer 1: Orb 1 (speed: 0.3)
Layer 2: Orb 2 (speed: 0.4)
Layer 3: Orb 3 (speed: 0.5)
Layer 4: Content (speed: 1.0)

Result: Depth illusion on scroll
```

### Number Counter
```
Start: 0
       ↓ (Incremental over 2s)
End:   250K+

Format: Adds commas/K suffix
Trigger: When section scrolls into view
```

### Scroll Indicator
```
     ↓
     ↓  ← Bounces (animation)
     ↓

Only visible in hero, fades on scroll
```

---

## 🎪 Easter Egg: Rainbow Mode

**Activation:** Konami Code (↑↑↓↓←→←→BA)

```
Normal Orbs:  ○ ○ ○ (Violet-Pink)
                ↓
Rainbow Mode: 🌈🌈🌈 (Hue-rotate 360°)
              Fast animation (3s vs 20s)
```

Console logs: "🎉 Easter Egg Activated!"

---

## 🖼️ Visual Preview Checklist

When viewing the website, you should see:

✅ Dark gradient background (purple tint)
✅ Three soft glowing orbs floating
✅ Sharp gradient text (violet to pink)
✅ Frosted glass cards
✅ Smooth hover effects (lift + glow)
✅ Animated number counters in stats
✅ Staggered card appearances on scroll
✅ Mobile menu slides in from right
✅ Scroll indicator bounces
✅ CTA buttons glow on hover
✅ Icons rotate slightly on hover
✅ Pro package stands out with border

---

*Use this guide to understand the visual design without opening the site!*
*Created by Fred - Session fred-2026-03-31-2255*

