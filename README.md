# Dr. Marvin's Marvelous Machines

> **Genius is a terrible burden.**
>
> No problem too small. No solution too elaborate.

A fictional mad-scientist invention studio for Instagram-first entertainment. Dr. Marvin treats humanity's most ordinary inconveniences as civilization-threatening emergencies, then responds with beautiful, ridiculous, surprisingly coherent contraptions.

**The character is mad. The solution has a brain.**

## Current state

- **Brand name:** Dr. Marvin's Marvelous Machines (locked).
- **Creator persona:** fictional eccentric inventor Dr. Marvin. He does not need an on-screen human likeness.
- **Visual direction:** gorgeous vintage patent engraving meets a mad inventor's notebook: warm ivory graph paper, meticulous dark ink, red handwritten indignation, generous negative space.
- **Social format:** four-slide portrait carousel, 1080 x 1350 px; Slide 1 uses **one AI-generated, text-free invention illustration** inside a deterministic HTML frame; Slides 2 to 4 are **fully HTML/CSS rendered**.
- **Closing ritual:** `GENIUS OR MADNESS?` with an invention-specific choice or question.
- **Console:** intentionally not built yet. This repo specifies its future inputs and rendering contract.
- **Publishing:** manual, never implied by completing a packet.

## The everyday workflow

1. Open a new ChatGPT conversation. Ask it to read `AGENTS.md` and follow the linked standards.
2. Say **"Give me 10 new machines."** ChatGPT reads the complete idea registry, produces ranked candidates, and records proposals when GitHub write access is available.
3. Choose **"Do #4."** ChatGPT develops one imaginative but physically intelligible invention, internally edits its copy, and produces one **console-ready JSON post packet** and one standalone illustration prompt.
4. Later, the console takes that packet, accepts **one illustration PNG**, renders four matching slides through locked HTML/CSS, exports four PNGs plus caption.
5. A human approves and posts. Record actual status; never invent publication or social performance.

The operator should not be asked to approve individual mechanisms, slides, captions, or intermediary artifacts. Only the idea selection and final creative judgment need human attention.

## Read this first

- [`AGENTS.md`](AGENTS.md): universal instructions for a fresh AI session.
- [`docs/BRAND_BIBLE.md`](docs/BRAND_BIBLE.md): brand identity, fictional world and character.
- [`docs/VOICE_AND_NAMING.md`](docs/VOICE_AND_NAMING.md): the distinctive Dr. Marvin sound, hooks, naming and comedy.
- [`docs/INVENTION_STANDARD.md`](docs/INVENTION_STANDARD.md): quality filter and plausible mechanics.
- [`docs/IDEATION.md`](docs/IDEATION.md): generate, rank, and deduplicate candidates.
- [`docs/POST_AND_VISUAL_STANDARD.md`](docs/POST_AND_VISUAL_STANDARD.md): exact slide jobs, typography, art direction.
- [`docs/PRODUCTION_WORKFLOW.md`](docs/PRODUCTION_WORKFLOW.md): selected idea to publishable package.
- [`docs/CONSOLE_CONTRACT.md`](docs/CONSOLE_CONTRACT.md): future interface, export, storage and JSON contract.
- [`docs/QA_AND_INTEGRITY.md`](docs/QA_AND_INTEGRITY.md): checks, claims and statuses.
- [`docs/CONTENT_STRATEGY.md`](docs/CONTENT_STRATEGY.md): audience promise, sustainable cadence, and what to learn from actual posts.
- [`prompts/START_A_CHAT.md`](prompts/START_A_CHAT.md): one copy-paste prompt and short commands.
- [`schemas/`](schemas/): JSON schemas for registry, ideation and post packets.
- [`ideas/registry.json`](ideas/registry.json): canonical deduplicated candidate list. Empty until the first ideation run.
- [`examples/`](examples/): one **illustrative, unapproved** package, used for calibration only.

## Scope and ownership

GitHub owns the instructions, schemas, copy packets, idea history, and small textual work products. The future console owns **deterministic rendering**, not rewriting. The illustration image and exported PNGs may live outside GitHub, but stable artifact references must be recorded in each post's packet.

Do not add n8n, Google Sheets, a complex dashboard, analytics plumbing, an autonomous scheduler, or multiple image generations to the ordinary workflow. This project's value is its creative originality and output, not the sophistication of its machinery.

## What is not yet finalized

The platform handle remains unverified. Working direction: `@drmarvininvents`. Proposed bio variant: "Turning minor inconveniences into major scientific breakthroughs. Genius is a terrible burden." This first sentence is a working candidate, not a confirmed lock. The editorial voice and brand name *are* locked.

The inaugural 25-idea slate, console implementation, account creation, actual image assets, and publication are separate future actions.
