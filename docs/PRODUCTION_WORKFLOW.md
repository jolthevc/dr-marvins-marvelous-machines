# From Selection to Console Packet v1.0

## The simple promise

The owner asks for ideas, picks one, and receives a complete imaginative invention packet. Later, the console renders the finished carousel from that packet plus one approved illustration. It should feel like one creative choice and one production action, not a multi-stage editorial committee.

## Stage 1: ideation

Read full registry, generate ranked concepts, deduplicate problem plus mechanism, score, allocate `MM-I####` IDs, persist `PROPOSED`, return list. Follow `docs/IDEATION.md`.

No deep research dossiers for each proposed idea. Quick product-category sanity check only when useful.

## Stage 2: user selects one concept

A simple command such as `Do MM-I0007` or `Do #7` authorizes full development and package generation. Resolve positional choices against the latest list in the active conversation, not against sorted IDs from another chat.

**Internal creative work, no review interrupt:**

1. Define the moment of pain and the current compromise.
2. Generate 2 to 3 credible mechanical approaches privately. Choose the most legible and ingenious.
3. Give the design one comic extravagance that dramatizes Marvin's obsession.
4. Write the final theatrical name, 1-line hook, problem diagnosis, three distinct features, and specific tribunal verdict.
5. Write the 35 to 75 word caption and the single text-free illustration prompt.
6. Perform research/novelty sanity check where possible. Record uncertain claims as concept assumptions, not verified fact.
7. Apply `QA_AND_INTEGRITY.md` and `schemas/post-packet.schema.json`. Revise until all mandatory fields pass.
8. Write one JSON packet and one optional human-readable review summary under `posts/`. Update registry state to `PACKAGED` and reference the artifact path.

No separate mandatory research approval, mechanism approval, title approval, script approval or caption approval.

## Stage 3: illustration (manual until console exists)

Generate one visual asset from `art_brief.prompt`. The image contains only the machine and its illustrated mechanics, no copy to be proofread. Apply the locked patent-notebook aesthetic.

Human may accept/regenerate if quality fails. This is the only normally bespoke graphic in the post.

Record a **real file path or durable asset URL** after it exists. Do not fabricate one. Set status `ILLUSTRATED` only after artifact confirmation.

## Stage 4: HTML console rendering (future feature)

The console:

1. Selects packet or pastes packet JSON.
2. Validates schema version, fields, copy lengths, four-slide cardinality, and referenced art.
3. Places image in the Slide 1 fixed frame.
4. Renders all overlay branding and copy from packet via locked HTML/CSS templates.
5. Renders Slides 2 to 4 wholly with HTML/CSS.
6. Exports exactly four `1080 x 1350` PNGs, caption in UTF-8, and optional ZIP.
7. Inspects actual output for overflow, missing image, sizing, clipped margins and readability before marking `RENDERED`.

**The console does not ask another AI to rewrite the packet.** All content decisions are upstream. No bespoke text/image placement per post.

## Stage 5: human posting

Human may approve and publish to Instagram. Posting remains manual by default. When a public URL and date are supplied or verified, record it with evidence/status in registry and packet sidecar if appropriate.

## File and ID naming

- Idea IDs: `MM-I0001`, `MM-I0002`... permanent.
- Post IDs: `MM-P0001`, `MM-P0002`... one canonical released concept per post, stable.
- Post JSON: `posts/MM-P0001-grand-luggage-hushifier.packet.json`.
- Human-readable brief (optional): `posts/MM-P0001-grand-luggage-hushifier.brief.md`.
- Art suggested basename: `MM-P0001-art.png`, only referenced when actually created.
- Rendered PNGs suggested `MM-P0001-01.png` ... `MM-P0001-04.png`.

IDs are backstage state, not prominent public design elements. Do not force an "Invention No. 0001" banner.

## Modification policy

Preserve canonical copy for a packaged post. A substantive creative revision increments packet `revision` and updates **all affected** fields: name, captions, hooks, poster prompt, problem, three features, verdict and art brief. Never leave a revised title with an image prompt referencing the old one.

An already generated illustration may become invalid after concept revision; require reapproval where mechanics changed. Do not silently overwrite live posted content. Keep prior version in Git history.

## Failure states

- Missing or conflicting idea: return the list and ask only for disambiguation that cannot be resolved.
- Image generation unavailable: save packet and complete art prompt; do not claim asset exists.
- GitHub write unavailable: present validated draft and mark it unsaved.
- No console yet: deliver packet, not fictional rendered PNGs.
- Actual output failed QA: do not mark rendered. Repair text/layout or regenerate only when necessary.

## Efficiency commitment

The standard workflow uses one idea selection, one structured creative pass (including internal review), one image generation, three deterministic editorial slides, and one export. Never add steps merely to imitate Green Knight's research operation or NCS's story development.
