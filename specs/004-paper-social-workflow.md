# Spec 004: Paper-to-social workflow

## Goal

Turn a newly published or accepted paper into a verified website update and platform-specific drafts without granting an AI permission to publish unreviewed claims.

## Workflow

1. Discover candidate works by OpenAlex author ID and created-date window.
2. Verify canonical metadata against Crossref and the DOI landing page.
3. Find lawful open-access locations through Unpaywall/OpenAlex. Never bypass access controls.
4. Build a fact sheet containing status, title, authors, venue, DOI, abstract-derived claims, code/data links, funding, image source and embargo state.
5. Produce distinct X, LinkedIn and website News drafts.
6. Move through `draft`, `review`, `approved`, `scheduled`, `published` or `rejected`.
7. Publish only after a named reviewer approves; archive platform post IDs and URLs.

## Acceptance criteria

- Default status is `draft`; no script publishes by default.
- A social draft references exactly one source publication or project record.
- Drafts record reviewer, review date, claims checked, image rights checked and embargo checked.
- X and LinkedIn copy are separate fields, not identical cross-post text.
- Publishing credentials never enter Git, Pages CMS content or generated site output.

