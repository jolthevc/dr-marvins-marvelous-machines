# Ideation Protocol v1.0

## Entry

Request: `Give me X new marvelous machines` or a directed variation such as `10 ideas about kitchens`, `5 more impractical ones`, or `ideas for commuting`.

Follow the precise requested count. Do not generate more candidates in the public answer merely because exploration produced additional rejected ones internally.

## Before ideation

1. Read `AGENTS.md`, brand, voice, invention standard and the **entire current registry**. Never rely on the last conversation's list.
2. Identify requested domain, sophistication and output count.
3. Deduplicate using three dimensions, not title alone: **problem**, **physical mechanism**, and **audience benefit**.
4. Search for existing products and near analogs when useful and possible; mark confidence honestly. Do not overresearch every quick idea.
5. Vary problem settings, physics, emotional triggers, complexity, and naming. Reject interchangeable product variations.

## Creative sequence

**A. Mine frustrations:** Start from scenes like noisy wheels, a wet sleeve, a missing sock, a door held open with groceries, a forgotten mug, or a tangle under a desk. Choose annoyances with emotional immediacy.

**B. Find the clever asymmetry:** What unexpectedly elegant physical action solves that exact moment? Focus on geometries, mounting, folding, clipping, sorting, indexing, diverting, damping, collecting, routing.

**C. Overshoot spectacularly:** Ask how a comically self-important scientist would dignify it. Add one delightful element without obscuring the real job.

**D. Name theatrically:** Use rules in `VOICE_AND_NAMING.md`. Avoid repetitive templates and sterile product names.

**E. Sketch mentally:** Can the full idea live in one rich patent-style hero drawing? If it is too invisible or too conceptual, weaken its rank or discard.

**F. Test the share impulse:** Can someone say "This is ridiculous, I need it" and send it to a friend who knows the exact annoyance?

## Scoring (editorial, not predicted social analytics)

Assign 1 to 5 in each dimension:

- **Relatability:** immediately understood annoyance.
- **Ingenious mechanism:** actual differentiated way to solve it.
- **Madness/comedy:** the serious, excessive Marvin angle.
- **Visual clarity:** beautiful, recognizable hero drawing.
- **Shareability:** surprising, quotable, friend-tagging potential.
- **Product desire:** credible emotional or practical appeal, despite absurdity.

Weighted score out of 30 is a simple sum. Break close ties using originality and variety rather than claiming a scientific virality model. A concept scoring under 3 for relatability or mechanism should normally be rejected or repaired before showing.

## Public ideation format

Begin with one sentence stating the selected creative angle. Then table:

| Rank | Idea ID | Marvelous Machine | The tiny catastrophe | The ingenious fix | Madness / 5 | Overall / 30 |

Then short cards for each idea, normally 4 or 5 lines max:

- Name + one-line theatrical hook.
- The ordinary annoyance and specific imagined mechanism.
- The comedic twist and the image we'd draw.
- Why it may be unusually shareable or desirable; one limitation if relevant.

End with **up to three** recommendations and why, but let the owner choose. Do not automatically create a post for a recommended idea unless requested.

## Registry protocol

Registry is canonical `ideas/registry.json`, validated against `schemas/registry.schema.json`.

- ID format `MM-I0001`, `MM-I0002`... Keep stable forever. IDs are internal only, not a banner in public visuals.
- Each presented new idea gets its own registry entry with status `PROPOSED`.
- Add aliases for alternate names. Do not create duplicate rows for naming variations.
- Mark intentional revisions via `related_ids`.
- Never delete or reuse an ID even if rejected. States include PROPOSED, SELECTED, PACKAGED, ILLUSTRATED, RENDERED, PUBLISHED, HOLD, REJECTED.
- Store normalized problem and mechanism independently to support semantic deduplication.
- When repo writes are available, save the proposals and return exact assigned IDs. On failure, use `[UNSAVED]` drafts without pretending registry was updated.
- Before any write, read latest registry to avoid clobbering another user's edits. Prefer a single commit for packet plus registry when tools support it; otherwise sequence writes carefully and reconcile failures.

## Freshness and research

Originality is an editorial judgment. If an analogous retail product exists, do not call the invention new to the world. Note the existing category or distinguish the whimsical twist. Viral predictions are hypotheses. Do not invent real-world performance evidence or consumer demand.

## Anti-generic test

If removing the character name leaves an interchangeable catalog product, strengthen the invention. If removing the product illustration leaves only a witty observation, strengthen the mechanism. It needs **both** a real invention idea and an unmistakable Marvin voice.
