# Spec 002: Structured content and CMS

## Problem

Most current content is raw HTML inside monolithic Markdown files. Routine edits require code changes and invite inconsistent facts.

## Required behavior

- Repeated content is stored as one Markdown file per person, project, publication, news item and social draft.
- Global group details are stored in `data/site.yaml`.
- Pages CMS is configured in `.pages.yml` with human-readable forms, media uploads and safe create/rename/delete operations.
- List and home templates render those collections without requiring HTML in content files.
- Draft records are excluded from the production site.

## Acceptance criteria

- An editor can add, edit, reorder and delete every repeated content type in Pages CMS.
- Publication fields include title, authors, venue, date, DOI, arXiv, code, data, project, OA URL and featured.
- People fields include role group, position, affiliation, bio, links, order, photo and alumni destination.
- CMS configuration parses as valid YAML and Hugo builds with unsafe Markdown disabled.

