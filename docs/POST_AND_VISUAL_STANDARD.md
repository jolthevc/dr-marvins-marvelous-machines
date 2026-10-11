# Four-Slide Social and Visual Standard v1.0

## The non-negotiable format

- Instagram portrait canvas **1080 x 1350 px** (4:5) for every slide.
- Four slides exactly by default. No filler slide and no fifth credits slide.
- **ONE** generated, text-free invention illustration, used on Slide 1. Slides 2 to 4 do not display this artwork; no additional image is generated.
- Slide 1: art is placed inside a stable HTML/CSS composition, which renders all type and markers.
- Slides 2, 3 and 4: fully deterministic HTML/CSS using text fields. No image generation for these slides.
- Labels and footer on all four: **DR. MARVIN** bottom-left, `0X / 04` bottom-right, optional small `FICTIONAL CONCEPT` notice where readable. Use no claim-like seals or patent numbers.
- A consistent site-level token system controls palette, type, margins, line weights and footers. The concept does not get a new palette every week.

## Visual north star

**The private sketchbook of a magnificently unhinged Victorian scientist, illustrated with the craft of an actual industrial patent engraver.** The page looks archival and handmade, but reading hierarchy is premium, modern and clear.

Not a literal blueprint, cyberpunk interface, photoreal luxury product ad, glossy 3D render, children's clip art, coffee-stained junk journal, scrapbook collage, or chaotic steampunk brass pile.

### Color tokens

| Token | Hex | Job |
| --- | --- | --- |
| paper | `#F2E8D3` | Warm archival ivory surface |
| ink | `#28241F` | Dark charcoal technical line and editorial titles |
| ink-soft | `#645949` | Secondary labels and notes |
| correction-red | `#A94235` | Handwritten indignation, focus markers, stamps |
| grid | `#C6BBA5` | Very faint measured grid, should recede |
| rule | `#B5A88F` | Rules, dividers, fine border details |

Consistent cream background, not random sepia/filter variation. Red should be scarce enough to feel like the scientist impulsively grabbed his correction pencil.

### Typography guidance for future HTML renderer

- Display/product names: expressive old-style serif, e.g. `Fraunces` or `Cormorant Garamond`, with stable font fallback `Georgia, serif`. Character without sacrificing mobile clarity.
- Main explanatory copy: `Source Sans 3` or similarly readable humanist sans, fall back `Arial, sans-serif`.
- Small engineering labels: legible mono-like, e.g. `IBM Plex Mono` or `Courier New`.
- Handwritten red notes: controlled cursive/handwriting face or carefully positioned fixed overlay; avoid illegible simulated handwriting or more than two short notes.
- Do not distribute proprietary font files. Define fonts by system/future web load when licensed.

### Composition and legibility

- Safety margins: **minimum 80 px** left/right and bottom for essential content on a 1080px wide render; allow additional clear space around logo and footer.
- Quiet header, strong central hierarchy, no crowded texture.
- Product illustration should occupy roughly 55 to 70% of Slide 1's visual area, depending on its silhouette.
- Main hook should be immediately readable without zooming. If name is long, use careful line break, not tiny body scale.
- Grid lines should be pale enough not to compete with the object.
- Avoid more than two handwritten red exclamations on Slide 1. Other annotations can be HTML and should earn their place.
- Layout must handle long names and short names without overflow, with preflight checks.

## Slide 1: The marvelous reveal

**Job:** Stop the scroll, let viewer identify the device, and hear Dr. Marvin's outrageous premise.

Recommended vertical hierarchy:

1. Small recurring header: `FROM DR. MARVIN'S LABORATORY` or `THE MARVELOUS MACHINE` (choose one canonical phrase in renderer).
2. Large illustrated mechanism, visually legible on phone.
3. Grand invention name, preferably 2 to 3 lines max.
4. The one-line hook, concise, characterful and instantly understandable.
5. Small `CONCEPT DESIGN` marking and standardized footer.

Artwork is text-free by default. The image model must NOT render brand names, titles, labels, numbers, or feature words into pixels. Text and labels belong to the renderer, which fixes spelling and consistency.

## Slide 2: The dreadful problem

**Header:** `A MOST DREADFUL PROBLEM` (fixed)

**Job:** Turn an ordinary annoyance into a bizarrely serious indictment, introducing the reader to Marvin's worldview.

- Optional tiny kicker: invention title.
- Main heading: a punchy 2 to 7 word indictment.
- Body: 35 to 70 words in one or two paragraphs, first person generally preferred.
- End with a cause-and-effect bridge toward the solution, not a cliffhanger copied from YouTube.
- Pure HTML, no need for a second image.

## Slide 3: The stroke of genius

**Header:** `THE STROKE OF GENIUS` (fixed)

**Job:** Reward curiosity with the genuinely clever design, rather than three adjectives.

- Three feature rows exactly, numbered `I`, `II`, `III` or `01`, `02`, `03` by the HTML template.
- Each feature has a witty 2 to 5 word name and a crisp 9 to 18 word physical explanation.
- Optional one-line mechanical thesis (up to 20 words).
- No product thumbnail or illustration. This slide is fully HTML/CSS typography and vector decoration only.
- All features should be nonredundant and plausible enough to envision physically.
- No claims of measured efficacy, prototype testing or patent grants.

## Slide 4: The audience tribunal

**Header:** `GENIUS OR MADNESS?` (fixed)

**Job:** Finish on a branded comic payoff with an actual conversation prompt.

- Strong verdict heading; preferably the header itself as the largest element.
- Specific 12 to 28 word dilemma tied to that invention, not generic "Thoughts?".
- HTML-rendered `GENIUS` and `MADNESS` visual labels as a recurring motif. They are **not interactive buttons**.
- Explicit, economical instruction such as `CAST YOUR VERDICT IN THE COMMENTS`.
- This slide is CTA-first, but it must feel like Dr. Marvin summoning a scientific tribunal, not a marketing intern begging for engagement.

## Captions

- 35 to 75 words usually, hard maximum 100.
- Two short paragraphs at most plus optional one-line concept disclosure.
- One fresh scene, Marvin's cure, and a specific question.
- Do not repeat all three feature descriptions and the Slide 2 paragraph.
- Optional `Genius is a terrible burden.` signature, not on every post.
- Avoid hashtags by default, excessive emoji, inauthentic scarcity, calls to buy nonexistent inventory.

## The illustration prompt contract

One generation only: editorial patent-quality mechanical drawing on flat or transparent background, preferably ink-only so renderer controls the parchment. The primary hero view is 3/4 perspective. Show the engineering features physically, avoid real product logos, legible wording and fake patent seals. A second tiny view within the *same* generated illustration is permissible when it clarifies workings without clutter. Black technical pen/engraved hatching, consistent visual realism, not plastic CGI.

The console should preserve illustration proportions; never stretch, crop away a mechanism, or place text directly over essential geometry. If image model supports transparent background, use it; otherwise match the warm paper token closely.

## Optional future enhancements

Do not launch with video, fancy effects, native app automation, real-time votes or more slides. A later Reel may animate a best-performing hero image or demonstrate a physical mockup, but never make this a requirement for ordinary production.
