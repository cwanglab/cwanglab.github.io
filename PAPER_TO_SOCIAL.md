# Paper-to-social operating procedure

## Current state

The repository can discover papers, verify DOI metadata and create a review record. It is not currently authenticated to X, LinkedIn or Buffer and therefore cannot publish or schedule a post. Account connection is a one-time owner action; API credentials must remain outside Git.

## Tool choices

| Need | Default | Why |
|---|---|---|
| Detect a new work | OpenAlex API | Stable author IDs, publication and record-created filters, DOI and location metadata |
| Verify formal metadata | Crossref REST API | Canonical DOI metadata from publishers and registration agencies |
| Find lawful full text | Unpaywall API, then OpenAlex locations | Open-access location, version and licence information without bypassing a paywall |
| Confirm author record | ORCID public API | Author-controlled public record; use as a cross-check, not the only alert source |
| Write and review | Pages CMS `Social queue` | One fact sheet and separate X, LinkedIn and website fields with an approval state |
| Schedule and publish | Buffer API/MCP | One integration for X and LinkedIn, drafts, queues, threads, media and metrics |
| Alternative publisher | Typefully API | Good multi-platform writing and scheduling workflow |
| Fully direct publishing | X API and LinkedIn Posts API | More control, but two developer apps, OAuth flows and ongoing API maintenance |

Do not scrape Google Scholar for monitoring. Do not copy a paper from an unauthorised source. Do not let an automated job publish a research claim without a named reviewer.

## Connect publishing accounts

1. Create a Buffer account and verify its email address.
2. In Buffer, open `Channels`: <https://account.buffer.com/channels>.
3. Connect the lab's X account while signed in to X as the account owner. X delegate access is not supported by Buffer.
4. Connect either the lab's LinkedIn Page or the PI's profile. A LinkedIn Page must be authorised through a personal LinkedIn account that is a Page **Super Admin**.
5. Set the timezone and posting schedule separately for each channel.
6. In Buffer, open **Settings -> API** only when API or MCP automation is required. Generate a key there and store it in a password manager or local environment variable, never in this repository.
7. Test with a Buffer draft assigned to one channel. Confirm the account, text, link and media before enabling any scheduling automation.

Buffer supports separate X and LinkedIn versions in one composer, X threads, LinkedIn Page/profile publishing and reviewable drafts. Relevant official setup references:

- X: <https://support.buffer.com/article/561-using-twitter-with-buffer>
- LinkedIn: <https://support.buffer.com/article/560-using-linkedin-with-buffer>
- API and MCP: <https://support.buffer.com/article/859-does-buffer-have-an-api>

## Setup

1. Find and confirm the PI's OpenAlex author ID. Merge/split errors are possible, so inspect the work list before using it for alerts.
2. Create a free OpenAlex API key and store it as `OPENALEX_API_KEY` outside Git.
3. Set `UNPAYWALL_EMAIL` to a real contact email for Unpaywall requests.
4. Run discovery for a recent window:

   ```bash
   OPENALEX_API_KEY=... python3 scripts/paper_watch.py discover \
     --author-id A123456789 \
     --from-date 2026-01-01 \
     --output /tmp/candidate-papers.json
   ```

5. Verify a candidate DOI:

   ```bash
   UNPAYWALL_EMAIL=... python3 scripts/paper_watch.py verify \
     --doi 10.1016/j.eswa.2026.131569
   ```

6. Create a private draft record:

   ```bash
   UNPAYWALL_EMAIL=... python3 scripts/paper_watch.py make-draft \
     --doi 10.1016/j.eswa.2026.131569
   ```

Open the result under `Social queue` in Pages CMS. Add the matching publication/project path, then write and review each platform field.

The website repository is public. Social queue files are excluded from the rendered Hugo site, but remain visible on GitHub after they are pushed. Do not place confidential peer-review details, embargoed results, unpublished claims, private contact information or access tokens in these files. Keep sensitive material in Buffer Drafts or a separate private repository.

## Draft rules

### Website News

- State what was published or released.
- Explain the research question and result in two to four sentences.
- Link DOI, open-access copy, code/data/project when available.
- Credit collaborators and funders accurately.

### X

- Lead with the research question or result, not “thrilled to announce”.
- Use one post when it fits; use a thread only when each post adds substance.
- Put the canonical DOI or project link in the post/thread.
- Tag coauthors only after confirming their preferred accounts.

### LinkedIn

- Use a short problem → approach → finding → significance structure.
- State limitations or study scope where omission would overstate the result.
- Credit team, institutions and funders in prose.
- Do not paste the X text unchanged.

## Approval gate

A reviewer must check:

- title, author order, venue and publication status;
- every quantitative or comparative claim against the paper;
- preprint, accepted-manuscript or version-of-record wording;
- funder and collaborator acknowledgements;
- image ownership/licence and patient/privacy concerns;
- journal or conference embargo;
- destination links and account tags.

Only then set status to `approved`. Scheduling or publishing through Buffer remains a separate authenticated action. Store resulting post IDs and URLs in the draft record.

## Day-to-day publishing

1. Run `make-draft` for the DOI or create a social queue record manually.
2. Complete the fact sheet and write separate X, LinkedIn and website News versions.
3. Have a named reviewer check claims, publication status, collaborators, funding, image rights and embargoes.
4. Set the record to `approved`.
5. In Buffer, create a new post, choose X and LinkedIn, then use **Customize for each network**.
6. Paste each approved version, attach a licensed figure or project image, add alt text and select **Set Date and Time**.
7. Confirm the scheduled posts in Buffer. After publication, record the public URLs and change the queue status to `published`.

Approval in Pages CMS never triggers publication by itself. This separation is intentional: metadata discovery can be automated, but public scientific claims require human review.
