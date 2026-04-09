
ROLE & MISSION
You are an expert front-end developer and UI/UX designer. Your task is to build a complete, modern, single-page personal portfolio website for Irfan, a 19-year-old IBDP Year 2 student based in Dubai, UAE. This site must feel premium, intentional, and compelling to competitive university admissions readers — particularly NYU. After every major section you build, use your live browser preview to visually inspect the layout, check for CSS overlap, verify mobile responsiveness, and confirm smooth scrolling before moving to the next section.

DESIGN SYSTEM — APPLY GLOBALLY
Palette:

Background: #F9F8F6 (warm off-white)
Primary Text: #1A1A1A (near-black)
Accent: #C8913A (warm amber/gold) — use sparingly for highlights, underlines, hover states
Secondary Text: #6B6B6B (cool grey)
Card Surfaces: #FFFFFF
Borders/Dividers: #E8E5E0

Typography:

Import from Google Fonts: Inter (weights 300, 400, 500, 600, 700)
Display headings: Inter 700, large, generous letter-spacing
Body: Inter 400, 1.7 line-height, comfortable reading width (max 68ch)
All caps labels/tags: Inter 500, 0.12em letter-spacing, small font size

Spacing & Layout:

Apple-style whitespace — sections should breathe, never feel cramped
Max content width: 1100px, centered
Section padding: minimum 120px top and bottom on desktop, 80px on mobile
Grid-based layouts using CSS Grid and Flexbox

Motion:

Subtle fade-up animations on scroll using Intersection Observer (no libraries)
Hover states on cards: slight translateY(-4px) + soft box-shadow
Smooth scroll behaviour on all anchor links: scroll-behavior: smooth

General Rules:

Mobile-first CSS, fully responsive at 375px, 768px, and 1280px breakpoints
No frameworks (no Bootstrap, no Tailwind) — pure HTML, CSS, JavaScript
Semantic HTML5 throughout
After building each section, open the browser preview and visually verify: no overlapping elements, correct font rendering, correct spacing on both desktop and mobile viewport sizes


SITE ARCHITECTURE — BUILD IN THIS ORDER

1. <head> & GLOBAL SETUP

Title: Irfan | Portfolio
Meta description: Personal portfolio of Irfan — filmmaker, leader, and IB student based in Dubai.
Viewport meta tag for mobile
Link Google Fonts (Inter)
Internal <style> block with all CSS (single file)
CSS custom properties (variables) for all colours, fonts, and spacing at :root
A sticky top navigation bar with:

Left: Name "Irfan" in Inter 600, accent colour on hover
Right: Nav links — About, Work, Leadership, IB, Contact
On mobile: collapse into a hamburger menu (pure JS, no libraries)
Background: #F9F8F6 with a subtle bottom border that appears on scroll




2. HERO SECTION
Layout: Full viewport height (100vh), vertically centered content, two-column on desktop (text left, image right), single column stacked on mobile.
Left column — text:

Small all-caps label in accent colour: DUBAI, UAE · IBDP YEAR 2
Large display heading (H1): Irfan — very large, bold
Subheading: Filmmaker. Storyteller. Leader.
A 2–3 sentence bio paragraph in secondary text colour:
"I build things from scratch — media outlets, documentaries, communities. Currently in my final year of the IB Diploma at GEMS Al Khaleej International School, I combine a passion for business strategy with a love for visual storytelling."
Two CTA buttons side by side:

Primary (filled, accent colour): View My Work
Secondary (outline): Get In Touch



Right column — image:

A circular or softly rounded portrait placeholder (use a grey gradient placeholder box with the label [Upload your headshot here] — make it easy to swap with a real <img> tag)
Subtle amber/gold ring border around the portrait

➡ VISUAL CHECK: Preview in browser. Confirm hero fills full viewport, text is readable, image placeholder is correctly positioned, and mobile stacking looks clean.

3. ABOUT / QUICK STATS STRIP
A full-width horizontal strip in white (#FFFFFF) with 4 stats displayed in a grid, separated by thin dividers:
StatLabel1,200+YouTube Subscribers2Award-Winning Short FilmsAED 2,000Raised for CharityBest SpeakerUNODC MUN 2024
Each stat: large bold number in accent colour, label below in secondary text colour. Clean, minimal, impactful.
➡ VISUAL CHECK: Confirm the strip is full-width, stats are evenly spaced, and on mobile they wrap into a 2×2 grid cleanly.

4. MEDIA & FILMMAKING SECTION
Section label: CREATIVE WORK
Heading: Filmmaker. Editor. Storyteller.
Subheading paragraph: Irfan is a multidimensional creative — a serious filmmaker with cinematic instincts, a content creator with business acumen, and a documentary storyteller driven by real people and real impact.
Layout: Two columns on desktop.
Left column — YouTube embed:

Embed the YouTube channel: https://www.youtube.com/@airmai4991/videos
Use a responsive <iframe> embed of the channel's latest video or a featured video
Label above: WATCH ON YOUTUBE
Below the embed, a text link styled in accent colour: View full channel →

Right column — skills & tools card stack:
Three white cards, each with:

An icon (use a simple SVG inline icon — camera, film reel, waveform)
Bold title
One sentence description

Cards:

Final Cut Pro — Professional-grade video editing for short films, documentaries, and school media content
Documentary Filmmaking — Produced and directed school documentaries distributed across GEMS Al Khaleej
Short Film Direction — Wrote, directed, and edited original short films, winning Best Director and Best Editor

➡ VISUAL CHECK: Confirm iframe is responsive, cards align correctly, no overflow on mobile.

5. AWARDS & RECOGNITION SECTION
Section label: RECOGNITION
Heading: Work That Gets Noticed
A horizontal scrollable card row (on mobile) / 3-column grid (on desktop) of award cards. Each card:

Accent-coloured top border (4px)
Award name in bold
Event/context in secondary colour
Year

Cards to include:

Best Director — School Short Film Festival · 2024
Best Editor — School Short Film Festival · 2024
Best Speaker — UNODC Model United Nations · 2024

Style: white cards, soft shadow, hover lift effect.
➡ VISUAL CHECK: Confirm cards are equal height, hover animation works, mobile scroll is smooth.

6. LEADERSHIP & COMMUNITY SECTION
Section label: LEADERSHIP
Heading: Building Communities From Scratch
Layout: Alternating left-right image+text rows (like an Apple product page). Use placeholder image boxes (grey gradient, labelled [Photo placeholder]) that can be swapped with real photos.
Row 1 — Middle School News (image left, text right):

Bold title: Middle School News
Tag: FOUNDER · EDITOR IN CHIEF
Description: Founded and led the school's first student-run news outlet in middle school, producing video content that became a staple of the school community. All video content edited and produced in-house.

Row 2 — High School Media Club (image right, text left):

Bold title: Media Club
Tag: FOUNDER · DIRECTOR
Description: Established GEMS Al Khaleej's high school Media Club, producing original documentaries screened and promoted across the school. Grew the club into a creative hub for student storytelling.

Row 3 — Student Council (image left, text right):

Bold title: Student Council
Tag: MEMBER · EVENT ORGANISER
Description: Organised and executed school-wide events including a charity bake sale that raised AED 2,000 for a local cause, and a lemonade stand fundraiser. Drove initiative, planning, and community engagement.

➡ VISUAL CHECK: Confirm alternating layout holds on desktop, stacks cleanly on mobile, placeholder boxes maintain aspect ratio.

7. MODEL UNITED NATIONS SECTION
Section label: PUBLIC SPEAKING
Heading: Best Speaker, UNODC · 2024
Layout: Full-width section with a dark background (#1A1A1A) for contrast — a "dark card" breaking up the light page rhythm.
Content (light text on dark):

Large pull quote styled prominently: "Representing ideas on a global stage requires clarity of thought and conviction of voice."
Below: paragraph describing Irfan's first MUN experience at UNODC committee, focusing on the debate between vigilantism and law enforcement, earning Best Speaker award
A small tag row: UNODC COMMITTEE · FIRST MUN · BEST SPEAKER AWARD

➡ VISUAL CHECK: Confirm dark section contrast is accessible, text is fully readable, no bleed issues at section edges.

8. IB & ACADEMIC SECTION
Section label: ACADEMICS
Heading: IB Diploma Programme · Year 2
Layout: Left column — subject list. Right column — Extended Essay feature card.
Left — Subject grid:
Display as a clean tag/pill list:

Business Management HL
Psychology HL
English A HL
Biology SL
Mathematics AI SL
German AB

Pills: white background, accent border, Inter 500.
Right — Extended Essay feature card:
Large white card with accent top border:

Label: EXTENDED ESSAY · BUSINESS MANAGEMENT
Title: Apple & AI: Redefining Business Strategy and Customer Experience
Description: An in-depth research paper examining how Apple's integration of artificial intelligence is reshaping its business model, product ecosystem, and customer relationships — analysed through both corporate strategy and consumer behaviour lenses.
Word count badge: 4,000 Words

➡ VISUAL CHECK: Confirm pill wrapping works correctly on mobile, EE card does not overflow its container.

9. CONTACT SECTION
Section label: GET IN TOUCH
Heading: Let's Connect
Layout: Centered, minimal. No form — just clean contact links.

A short line: "Open to university connections, creative collaborations, and opportunities."
Three icon+link rows:

📧 Email placeholder: [your email here]
🎬 YouTube: youtube.com/@airmai4991
📍 Location: Dubai, UAE



Style each as a pill/button with hover accent colour. Keep it spacious and uncluttered.

10. FOOTER
Minimal single-line footer:

Left: © 2025 Irfan. All rights reserved.
Right: Built with intention.
Thin top border in #E8E5E0
Font: Inter 400, small, secondary text colour


FINAL QUALITY CHECKLIST — RUN IN BROWSER BEFORE DELIVERING
After completing all sections, perform the following checks using your live browser preview:

Scroll the full page — confirm smooth scrolling, no layout jumps, no orphaned elements
Resize to 375px width — confirm every section stacks correctly, no horizontal overflow, no text clipping
Resize to 768px width — confirm tablet layout transitions correctly
Hover all interactive elements — cards, buttons, nav links — confirm transitions are smooth
Click all nav links — confirm anchor scroll works and lands correctly
Check z-index layering — sticky nav must sit above all content while scrolling
Check font rendering — Inter must load from Google Fonts, fallback to system-ui, sans-serif
Confirm no console errors in the browser dev tools
Confirm all placeholder image boxes are clearly labelled and easy to swap
Confirm the amber accent colour appears consistently and never feels overwhelming

Deliver the complete, working single HTML file with all CSS and JS internal. No external dependencies except Google Fonts.

