# Content administration

## Current state

The editor configuration exists locally but has not been pushed to GitHub yet. Pages CMS reads `.pages.yml` from GitHub, so the new editing forms will not appear until the current site changes are committed and pushed to `cwanglab/cwanglab.github.io`.

## Open the editor

1. Visit `https://app.pagescms.org` or the deployed site's `/admin/` shortcut.
2. Choose **Sign in with GitHub** using an account with write access to the `cwanglab` organisation.
3. Install or authorise the Pages CMS GitHub App. Limit repository access to `cwanglab/cwanglab.github.io` unless broader access is intentionally required.
4. Open `cwanglab/cwanglab.github.io` and select the `main` branch.
5. Pages CMS reads `.pages.yml` and shows forms for site settings, research, people, publications, projects, news and the non-confidential social queue.

Pages CMS is the editing interface, not a separate hosting system. Its official hosted setup is GitHub sign-in, GitHub App installation, repository selection and then editing: <https://pagescms.org/docs/quick-start/>.

## What to edit

| Editor area | Use it for |
|---|---|
| Site settings | Lab name, institution, mission, contact details and profile links |
| Research directions | Research text, figures, captions, source links and display order |
| People | Members, roles, biographies, photographs and academic links |
| Publications | Verified bibliographic metadata and DOI, open-access, code and data links |
| Projects and code | Project summaries, status, images and outputs |
| News | Public website announcements; leave `draft` enabled until checked |
| Social queue | Publishable copy and workflow status only; never confidential review notes |

## Save and publish

1. Open or create a record and complete the required fields.
2. Use the preview where available and save the record.
3. Pages CMS writes a Git commit to the selected branch.
4. Confirm the GitHub Pages workflow succeeds.
5. Check the resulting page on the public website, including its links and images.

Pages CMS edits the Markdown and YAML files directly. There is no separate production database to back up. Every edit is a Git commit and the existing GitHub Pages workflow rebuilds the site after a change reaches `main`.

## Additional accounts

Use named accounts rather than one shared password:

| Role | Recommended account | Access |
|---|---|---|
| Site administrator | A separate GitHub account with `cwanglab/cwanglab.github.io` access and two-factor authentication | Content, media, `.pages.yml`, collaborators and repository settings |
| Content editor | A Pages CMS collaborator invited by email | Content and media only; no CMS configuration or collaborator management |

Pages CMS collaborators are repository-scoped and can edit content without GitHub repository administration. The hosted Pages CMS service does not define a local username/password in this website repository. An independent password-based administrator would require a self-hosted CMS, PostgreSQL, a GitHub App, email delivery and a maintained authentication service.

Do not add a JavaScript-only password form to `/admin/`. GitHub Pages is static, so its password and protected content would be downloadable and bypassable. The existing `/admin/` path is intentionally only a shortcut to the authenticated Pages CMS service.

## Editorial rules

- Do not publish a person or photograph without consent.
- Do not add citation counts, h-index, funding totals or team counts unless the source and “as of” date are shown.
- Use a DOI URL for published papers and label preprints as preprints.
- Set `draft: true` for unfinished News records.
- Social queue records are not rendered by Hugo, but they are visible in a public GitHub repository. Store only material that is safe to disclose. Use Buffer Drafts or a separate private repository for confidential review notes.
- Moving a social record to `approved` documents approval; it does not itself publish anything.

## Images

Upload images through the Images media area. Use real group, equipment, project or research images and add explanatory text in the page body. Confirm ownership or reuse permission before uploading. Do not use publisher figures unless their licence permits reuse.

## Collaborators

Pages CMS collaborators can be invited by email for content editing without giving them repository administration. Restrict configuration and GitHub settings to site maintainers.
