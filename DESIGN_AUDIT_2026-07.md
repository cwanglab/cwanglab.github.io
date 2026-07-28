# Design audit and type/layout specification — HTIL website

**Date:** 28 July 2026
**Subject:** `cwanglab-v2` (current, adopted) measured against `cwanglab.github.io` @ d253170 (previous generation) and against 16 top-lab sites
**Method:** computed-CSS measurement via Chrome DevTools Protocol at 1440px, pixel scans of 1:1 screenshots, ink-bounding-box analysis of every SVG, Crossref resolution of every DOI, and adversarial refutation of every high/critical finding. Numbers in this document were measured, not estimated. Where a finding was refuted it is recorded as refuted and not acted on.

---

## 1. Verdict

### Plain language

v2 is an honest, careful, entirely unremarkable academic site. Nothing on it is false. Nothing on it is embarrassing. Nothing on it makes a case.

A hiring chair at Oxford or ETH who spends three minutes here learns the group's org chart and nothing about what it has found. The first content block after the hero is a self-drawn three-box Cloud→Edge→Terminal diagram — a taxonomy the group did not invent (arXiv:2508.18803 is a survey of the same term) containing no data, no result and no number, occupying 840px of a 4,470px homepage. The two Nature Communications papers, which are the only facts on this site that would make a senior reader keep reading, sit at y≈3,850 of 4,470 — the sixth of seven sections, below the staff roster — described by cohort size rather than by finding. That is the whole verdict. Everything else in this document is smaller than that.

v1 is worse and the reason is not aesthetic. Its homepage hero read "h-index 25 · 3,400+ citations · 72 publications · 8 PhD researchers · 5 multicentre RCTs" (`/tmp/site-v1/layouts/index.html:8`). Against `CV/c_cv2.tex`: the CV lists 11 current PhD students, not 8 (lines 485–496); it contains two NCT identifiers, not five, and DIAMOND and SALTIRE II appear nowhere in it; its own role strings for those trials are "RA" (line 355) and "PhD Researcher" (line 358), not "AI lead"; the PI funding lines sum to roughly £289K against a claimed "£430K+ as PI"; the £1.8M BHF award is recorded as "Named Researcher" but counted toward "£2.4M+ as Co-Investigator". Its team page rendered eight anonymous DiceBear cartoon faces captioned "PhD Researcher", and rendered Assoc. Prof. Marta Vallejo — a real, named woman — as a cartoon man in a necktie. Any single one of those is survivable. On one page they establish a pattern, and reviewers do check Gateway to Research and ClinicalTrials.gov. **Nothing from v1's metrics readout, funding figures or trial list may be ported into v2 under any circumstance.**

### Scores

| Dimension | v2 | v1 | Basis |
|---|---|---|---|
| Truthfulness of stated claims | 9.0 | 4.0 | v2: 9/9 publication DOIs resolved against api.crossref.org, every returned title/journal/author list matches the site string exactly; zero superlatives across a full grep of `content/` and `layouts/`; 50,226 and 48,608 both verbatim in PMC11697225. v1: five unreconcilable claims on one page (above). |
| Evidence of a track record | 6.5 | 5.0 | v2 publishes 9 of 82 CV items and omits the PI's own April 2026 corresponding-author ISBI paper (Crossref 10.1109/ISBI61048.2026.11515308, two current members as co-authors). No patent, grant, or trial appears anywhere. v1 carried the numbers but two of them did not reconcile. |
| What a panel actually takes away | 5.5 | 4.5 | Section order measured from content bands: Nature Comms at 86% page depth in v2; v1 put them at 44% but with no author lines and no DOIs on seven high-citation entries, one of which (MM-WHS) appears nowhere in `c_cv2.tex`. |
| Typography against 12-lab benchmark | 6.5 | 6.0 | v2 passes 5 of 8 measured standards outright (alignment 12/12 pairs vs benchmark 91%; measure 760px/91ch inside the 540–850px band; 17px/1.65 inside 16–20px and 1.40–1.75; flush-left; no-webfont is a legitimate 5/12 minority). Fails serif headings (0/12 precedent) and uppercase tracking (1 of 11 rules vs benchmark 14/14). |
| Alignment and layout discipline | 5.0 | 4.0 | v2: 7 of 13 pages have exactly one left edge at x=160; the other 6 have 2–4. v1: header/hero/footer at x=236 against all body text at x=340, a 104px jog on every page, plus 22 section eyebrows printed above their own section rule. |
| Figures — draughtsmanship | 6.5 | 0 | v2 has five purpose-built schematics with an exact 6-colour palette matching the CSS tokens and zero gradient/filter/shadow elements. v1 has no diagrams at all; its only 11 SVGs are cartoon avatars. |
| Figures — deployment | 3.0 | — | Four homepage diagrams render their labels at 4.41–7.43 CSS px; two paper crops served at 1.00× and 1.15×; three paper crops orphaned. |
| Front-end engineering | 7.0 | 7.0 | Zero-dependency inline CSS, correct responsive disclosure at ≤1000px, byte-identical geometry at 1280 and 1440. Offset by 47 of 71 baseof classes being dead. |
| **Overall** | **6.2** | **4.8** | Consistent with the 23 July head-to-head (6.7 / 5.3); the gap widens once v1's unsupportable metrics are counted. |

### The honest ceiling

**With every CSS and figure defect in this document fixed and no new content, this site tops out at about 7.5/10.** It would be clean, well-linked, honest and unremarkable — which is a fair description of MIT PDOS and karpathy.ai, both of which are fine.

Two things stand between 7.5 and 8.5, and neither is typographic:

1. **Photographs.** Zero on either generation. `static/images/people/` contains only `.gitkeep`; `photo:` is empty in 36 of 36 files under `content/people/`. This is hard standard 7 in the PI's own survey (`cwanglab_website_review.md:28`) and the only one all 35+ surveyed sites meet. Blocked on `CONSENT_EMAIL.md`.
2. **A finding, stated as a finding, above the fold.** The homepage currently says "measuring bone marrow adiposity in around 47,000 UK Biobank participants" — a method and a sample size. The heritability estimate, the genome-wide significant loci and the Mendelian randomisation link to fracture risk are on `content/projects/bone-marrow-adiposity.md:20`, four clicks away.

Both need the PI. No amount of letter-spacing substitutes for either.

### Credibility defects versus untidiness

Sort everything on this site into two piles. The distinction matters because they have completely different fix priorities.

**Costs credibility** (a senior reader forms an adverse judgement):
- The footer "Research profiles → GitHub" on all 48 pages points to `github.com/cwanglab`, whose live API bio reads "Full-stack developer. Open source contributor.", company "Independent", location "San Francisco, CA", 0 followers, and whose 8 repos are dotfiles, a Coolify fork, a TLS-scanner fork and the two site repos. No research code. This is the one link on the site that leads somewhere damaging.
- `content/research/medical-imaging.md:7-8` supplies alt text and a caption describing a figure about cross-scanner reliability; the drawing (`dir-medical-ai.svg`) is a four-step MRI→measurement→PheWAS/GWAS→clinical pipeline. The SVG's own `aria-label` contradicts the page's caption.
- 11 DiceBear "Notionists" cartoon SVGs — including caricatures of two named senior academics from the v1 team page — are still git-tracked, still built, and still return HTTP 200 at `/avatars/pi.svg`.
- The ISBI 2026 paper is missing from `content/publications/` while being the group's most recent conference output with the PI as corresponding author.
- Four homepage diagrams whose text renders at 4.41–7.43px. Illegible type is not neutral: it says nobody opened the page at the size it ships.

**Merely untidy** (nobody outside will notice, fix when convenient):
- 47 of 71 baseof CSS classes are dead (verified today: 48 built pages, 107 orphaned rule blocks). Real cost: 1.4 KB gzipped per page and a maintenance hazard. Zero reader-visible cost — stripping them produces a pixel-identical homepage render.
- 30 declared font-size values, 38 spacing values, three list indents (22 / 24 / 28px).
- The 45px inset between `framework.svg`'s ink and its caption. **Refuted as a defect**: the SVG carries a symmetric 60/60/50/64-unit internal margin, i.e. a conventional figure bounding box, and MIT HAN Lab's homepage figures carry comparable and *asymmetric* insets (61px left vs 41px right). Do not chase this on its own; it falls out of the viewBox tightening in §3.5 anyway.

### Two contradictions in the source audits, resolved

**(a) The homepage's "around 47,000".** Two audits filed this as a numerical inconsistency against the 50,226 used elsewhere and recommended changing it. **This was refuted and must not be actioned.** The PMC11697225 abstract reads verbatim: "we use deep learning to measure bone marrow adiposity … from MRI scans of approximately 47,000 UK Biobank participants". Git history shows commit e891193 changed the homepage to 50,226 and commit 771c850 changed it back 40 minutes later with the reasoning recorded in the message: 50,226 is the imaging-batch size, 48,608 the post-QC retained set, ~47,000 the number actually measured. The site uses each number for the claim it belongs to. Changing it would assert that 50,226 participants were measured, which is false. The one loose surface is `dir-medical-ai.svg:18`, which carries a bare unqualified "50,226 participants" with no "batches" wording to scope it — that is the label to tighten, not the prose.

**(b) Georgia headings: strength or defect?** The typography benchmark found zero serif families across 19 first-choice families on 12 top-lab sites and filed Georgia headings as a high-severity defect. The panel-lens audit filed "serif headings" as a strength contributing to a register of confidence. **Resolution in §3.7: keep Georgia.** Reasoning there.

---

## 2. The alignment problem, answered with numbers

The PI's complaint is correct in substance and narrower in cause than "the alignment is bad everywhere". The skeleton is sound: 497 of 497 measured text nodes compute to `text-align: start` — nothing on this site is centred or justified, which is the single most important typographic decision on an academic page and it is right. The damage is in six specific places, and it is a measurable regression against v1 on three axes.

### 2.1 Left-edge census (13 pages, computed at 1440px, confirmed by pixel scan)

| Page | Distinct left ink positions for block text | Detail |
|---|---|---|
| `/about/`, `/news/`, `/news/*`, `/projects/`, `/projects/*`, `/publications/`, `/research/` | **1** | All at x=160. This is a professional result and covers 7 of 13 pages. |
| `/people/` | **3** | Section headings and monogram circles at x=161–163; member body text at x=257; PI body text at x=285. |
| `/opportunities/` | **4** | Paragraphs x=161; `<ol>` text x=184; `<ul>` text x=189; `<h2>` glyphs x=207. |
| homepage | **2** (plus figure) | Text at x=160–165; `framework.svg` ink at x=205–206. |

The `/people/` stair-step is caused by `layouts/people/list.html:9` setting `.member { grid-template-columns: 76px minmax(0,1fr); gap: 20px }` and line 10 overriding it for the PI with `104px minmax(0,1fr)` at the same gap: 160+76+20 = 256 versus 160+104+20 = 284. It falls exactly at the boundary between the PI and the students, which is the most-scrutinised transition on the site.

The `/opportunities/` fan-out is caused by `layouts/opportunities/list.html:5` (`.opp h2 { padding: 20px 0 0 46px }` with an absolutely-positioned `::before` counter at left:0), line 17 (`ol` padding-left 24px) and lines 20–21 (`ul` padding-left 2px + `li` padding-left 26px = 28px effective).

Three list indents coexist: 22px (`layouts/index.html:19`), 24px (`baseof.html:128`), 28px (`opportunities/list.html:20-21`).

v1, for comparison, had 1–3 left edges per page — but with a structural 104px jog between its header/hero/footer container (x=236) and its body container (x=340) on all four pages measured. Both containers were centred on x=720, so v1's is a concentric nested-container convention rather than a misalignment; v2's is flush-left with local breaks. Neither is strictly "more aligned". v2's convention is the better one and the breaks in it are cheap to close.

### 2.2 Measure census

`--measure: 760px` is declared at `baseof.html:58` and genuinely referenced 12 times across the layouts (verified today). It is then abandoned in four places:

| Element | Width | Characters/line at its own size | Source |
|---|---|---|---|
| Standard prose | 760px | 91ch @ 17px Arial | `baseof.html:123`, `:115` |
| `.page-head h1` | 900px | — | `baseof.html:114` |
| `.member--pi` bio | 996px | **135ch @ 16px** | `people/list.html:10`, block spans `grid-column: 1 / -1` |
| `.opp-cta` | 1066px | 151ch | `opportunities/list.html` |
| `.pub` entries | 1120px | 1–2 lines only | `publications/list.html` inherits `.shell` |
| `.framework-figure` | 1080px | — | `index.html:25` |
| `.dir-text` | 454px | 52–60ch | consequence of `index.html:33` |

Right-edge census across the 13 pages: **8 distinct values** — 696, 760, 920, 960, 1060, 1240, 1253, 1280. Two of them account for most of the page area (920 for 117 blocks, 1280 for 82).

Two of these are **not** defects, and the spec in §3 preserves them:

- **`.pub` at 1120px is fine.** Bibliographic records are not prose. No entry on `/publications/` exceeds two lines (6 of 9 titles are one line). MIT HAN Lab runs its 92 citations at 1024px; zlab.bio at 1079px. Capping them would cost 6.3% page height and leave 520px dead at 1440.
- **`.dir-text` at 454px is fine, and is better than the alternative.** 52–60 characters is inside the 45–75 band; removing the thumbnails to "recover the full measure" would put those paragraphs at 86–90ch, past the WCAG 1.4.8 80-character guidance. MIT HAN Lab uses a ~400px text column beside a figure. The thumbnails' problem is legibility (§4), not the column they create.

The PI's bio at **135 characters per line** is the one that matters. The peer convention does permit a wide PI row — HAN Lab's own PI bio measures 941px / 129ch — so the width alone is not disqualifying. The visible defect is the *within-page* jump: a 69ch intro paragraph and a 135ch bio on the same page, at the top, in the block a hiring chair is most likely to read start to finish.

### 2.3 Label-column census

Only two label columns actually render:

| Class | Column | Gutter | Status |
|---|---|---|---|
| `.member` | 76px | 20px | live |
| `.member--pi` | 104px | 20px | live — the 28px stair-step |
| `.theme` | 180px | — | dead |
| `.publication-year` | 110px | — | dead |
| `.news-item` | 130px | 34px | dead in effect (`news/list.html:9` overrides to `display:block`) |
| `.person--pi` | 230px | — | dead |
| `.research-detail-head__grid` | 280px | — | dead |

Seven mutually inconsistent label-column widths exist in the stylesheet; five are unreachable. That is the mechanism by which the two live ones came to disagree — nobody could see which were real.

### 2.4 Figure-versus-text alignment

Measured ink bounding boxes, rendered at 1400px on white, threshold channel-sum < 755, expressed in viewBox units:

| File | viewBox | Ink | L / T / R / B margins | Dead canvas |
|---|---|---|---|---|
| `framework.svg` | 1400×520 | 1282×408 | 59 / 49 / 59 / 63 | 28.2% |
| `dir-terminal.svg` | 560×420 | 521×312 | 29 / 54 / 10 / 54 | 30.8% |
| `dir-robotics.svg` | 560×420 | 536×331 | 14 / 44 / 9 / 44 | 24.5% |
| `dir-heterogeneous.svg` | 560×420 | 522×374 | 19 / 37 / 19 / 9 | 21.5% |
| `dir-medical-ai.svg` | 560×205 | — | 10 / 19 / 10 / 11 | 17.7% |

Consequences at the served sizes: `framework.svg`'s `<img>` box left-aligns with the text column at x=160.0 exactly, but its first drawn rectangle starts at x=205–206 — a 45px optical inset. Its 63-unit bottom margin becomes 48.6 px of blank, so although the CSS sets the figcaption 6.0 px below the image box, the *visible* gap from the last drawn element to the caption is 54.6 px. `dir-terminal.svg` has left and right margins differing by a factor of 2.9, so its composition sits visibly right of centre. `dir-heterogeneous.svg` has a top margin 4.1× its bottom, and its caption at y=408 sits 9 units off the canvas edge.

The 45px inset is **not** in itself a defect (refuted; symmetric figure margins are the benchmark norm). The asymmetries and the 54.6px caption gap are.

### 2.5 Type-scale count

Verified today: `grep -rhoE 'font-size: *[0-9.]+px' layouts` yields **30 distinct values** — 10, 11, 12, 13, 14, 15, 15.5, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 34, 35, 39, 40, 44, 45, 48, 58.

Five of them (19–23) sit inside a 4px band. Four (26–29) sit inside a 3px band. Benchmark: median 6.5 *rendered* sizes per homepage across 12 sites (MIT PDOS 2, BAIR 3, HAN Lab 4, Hinton 4, CSAIL 5, zlab 6, VGG 7, MLG 7, karpathy 7, SAIL 8, THUNLP 8, ETH 11). v2 renders 10 on the homepage — inside range. The problem is the source, not the render.

One correction to the source audits: they reported "four different desktop h1 sizes including a 44px/45px pair". Two of those four (`.home-hero` 58px, `.research-detail-head__copy` 45px) are dead classes. The live h1 sizes are **two**: 44px (`.page-head h1`, `baseof.html:114`) and 40px (`.home-intro h1`, `index.html:10`). Still two too many for one role, but the 1px pair does not ship.

Leading is worse than size count: **26 distinct size/line-height pairs**. 22px appears with 1.25, 1.30 *and* 1.65. 15px with 1.50, 1.60 and 1.65. Because the same size gets different leading in different components, no two blocks can share a vertical rhythm. This is what produces the diffuse impression of unprofessionalism that has no single pointable cause.

Spacing: 38 distinct non-zero px values; 15 of 38 fall on a 4px grid, 8 of 38 on an 8px grid. 12, 13, 14, 15, 16 all coexist, as do 24, 25, 26, 28, 30, 32, 34, 36, 38.

### 2.6 Uppercase tracking

Verified today. Eleven `text-transform: uppercase` rules exist in `layouts/`. **One** sets `letter-spacing`:

```
layouts/projects/list.html:5   .project-item__area   letter-spacing: 0.06em   ✓
layouts/_default/baseof.html:89   .brand__meta        10px   — none
layouts/_default/baseof.html:98   .kicker             13px   — none
layouts/_default/baseof.html:109  .framework-item__label     — none  (dead)
layouts/_default/baseof.html:138  .record__meta              — none  (dead)
layouts/_default/baseof.html:193  .publication__links        — none  (dead)
layouts/_default/baseof.html:197  .news-item__date           — none
layouts/_default/baseof.html:204  .detail-meta dt            — none  (dead)
layouts/_default/baseof.html:210  .footer-grid h3     12px   — none
layouts/projects/single.html:5    .project-detail__meta dt   — none
layouts/partials/publication-single.html:13  .pub-single__facts dt  — none
```

Benchmark: **14 of 14** uppercase micro-label instances across the sample carry positive tracking, +0.045 to +0.083em (MIT CSAIL 10px/+0.83px and 12px/+0.86px; THUNLP 14px/+1px ×7; HAN Lab 14px/+1px; Oxford VGG 11px/+0.5px). The only untracked uppercase found anywhere in the benchmark is Oxford VGG's 13px bold *nav bar* — not a micro-label. Eight of twelve sites use no uppercase micro-labels at all.

This is the most consistent rule found in the entire benchmark, the cheapest to satisfy, and **a regression**: v1 tracked 4 of its 6 uppercase rules, at 0.07em–0.16em, and rendered 18 of 18 uppercase instances with tracking.

### 2.7 The `.kicker` specificity bug

`baseof.html:98` declares `.kicker { margin: 0 0 15px; color: var(--claret); font-size: 13px; font-weight: 700; text-transform: uppercase }` at specificity 0-1-0. Every kicker in the codebase is a `<p>` inside `.page-head` or `.home-intro`, so it is always beaten by `.page-head p { color: var(--muted); font-size: 20px }` (`baseof.html:115`, 0-1-1) or `.home-intro p { font-size: 19px }` (`index.html:6`, 0-1-1). Measured across 12 pages: 11 render at 20px grey, one at 19px claret. **None renders at 13px.** Mobile is also affected (`baseof.html:251` sets 18px, `index.html:41` sets 17px). 39 of 48 built pages carry a kicker.

Visually this is milder than it sounds — the 20px grey sans eyebrow is still clearly subordinate to the 44px near-black serif h1, and a panel member would not consciously register it. The one visible symptom is on the homepage, where the 19px kicker overflows the 760px measure and wraps with "UNIVERSITY" widowed on its own line (confirmed by screenshot). It is worth fixing as a one-line change that restores the author's stated intent on 39 pages, not because it costs credibility.

### 2.8 Dead CSS

Rebuilt clean and re-verified today: 48 built HTML files, 71 classes declared in the `baseof.html` `<style>` block, **47 never appear in any built page**, accounting for 107 rule blocks and 9,127 of 15,593 rule bytes (58.5%).

Cause is git-provable. Commit `1b531de` ("Return to classic academic lab style") rewrote nine page templates with new page-scoped CSS (`.home-intro`, `.member`, `.pub`, `.project-item`, `.research-list`) and **touched `baseof.html` zero times**, leaving the superseded globals (`.home-hero`, `.person`, `.publication`, `.record`, `.theme`, `.research-card`) in place. Six component families now exist under two names each.

Wire cost: 1,432 gzipped bytes per page, 16.9% of an 8.5 KB gzipped homepage. Reader-visible cost: zero — stripping all 107 blocks from the built homepage produces a byte-identical render. This is a maintenance hazard, not a design defect, and it is ranked accordingly in §5.

One live collision remains: `baseof.html:196` defines `.news-item` as a 130px two-column grid and `layouts/news/list.html` overrides it with a `.news-feed .news-item` prefix specifically raised to win, with a comment in the file admitting so.

---

## 3. Type and layout specification

This is the fix, written so it can be implemented without further judgement calls. Every value carries either a benchmark measurement or a stated principle.

### 3.1 Type scale — seven steps, no others

Declare in `:root` at `layouts/_default/baseof.html:44`:

```css
--t-1: 12px;   /* uppercase micro-label, footer headings, metadata dt   */
--t-2: 14px;   /* metadata, positions, link rows, small body            */
--t-3: 17px;   /* body — the default reading size                       */
--t-4: 20px;   /* page deck / lead paragraph                            */
--t-5: 24px;   /* h3 — member name, list item title                     */
--t-6: 30px;   /* h2 — section heading                                  */
--t-7: 40px;   /* h1 — one size, every page                             */
```

Ratios 1.17 / 1.21 / 1.18 / 1.20 / 1.25 / 1.33 — regular and slightly expanding, which is standard for a display scale. Seven steps against a benchmark median of 6.5 *rendered* sizes per homepage and a mode of 7.

Anchors and their justification:
- **17px body** is the benchmark median exactly (MIT HAN Lab 20, Oxford VGG 15, Stanford SAIL 16, CSAIL 18, ETH 20, Cambridge MLG 17, BAIR 16, Hinton 16, PDOS 16, karpathy 17, zlab 17.68). It is already what the site uses. Do not change it.
- **12px floor** matches the benchmark micro-label range (10–14px) and is the site's existing smallest live size.
- **40px h1** collapses the two live h1 sizes (44 and 40) into one. Benchmark h1s range 24px (Hinton) to 68.4px (Stanford SAIL); 40px is unremarkable in that range and is what the homepage already uses.

Required mapping (do not improvise substitutions):

| Current | New | Where |
|---|---|---|
| 44px, 40px | `--t-7` 40px | `.page-head h1`, `.home-intro h1` |
| 26px | `--t-6` 30px | `.member-group h2`, section h2 |
| 26px, 22px | `--t-5` 24px | `.member--pi h3`, `.member h3` — PI hierarchy is carried by the full-row span, not by a larger name |
| 21px, 20px, 19px | `--t-4` 20px | `.page-head p`, `.home-lead`, `.home-intro p` |
| 18px, 17px, 16px | `--t-3` 17px | all body prose |
| 15.5px, 15px, 14px | `--t-2` 14px | metadata, summaries, positions |
| 13px, 12px, 11px, 10px | `--t-1` 12px | all uppercase micro-labels including `.kicker` and `.brand__meta` |

**Line-height: exactly two ratios.**
- `1.6` for everything at `--t-4` and below.
- `1.2` for everything at `--t-5` and above.

Benchmark median ratio is 1.50 and the range is 1.40–1.75. The site currently runs 1.65 at 17px, which is generous and slightly favours readability at 91 characters. 1.6 keeps that and removes the 26 ad-hoc pairs.

### 3.2 Spacing scale — eight values, base 4

```css
--s-1: 4px;  --s-2: 8px;  --s-3: 12px; --s-4: 16px;
--s-5: 24px; --s-6: 32px; --s-7: 48px; --s-8: 64px;
```

Every margin, padding, gap and offset in the site uses exactly one of these. Nothing else. This replaces 38 ad-hoc values of which only 15 currently fall on a 4px grid.

Consequence to apply immediately: list indent becomes `--s-5` (24px) everywhere. Delete the 22px override at `index.html:19` and the 2px/26px pair at `opportunities/list.html:20-21`; keep `baseof.html:128` at 24px.

### 3.3 One content measure

**760px = 91 characters at 17px Arial** (measured on `/research/`; capacity is 96 characters).

Justification: the three benchmark sites that declare an explicit prose container cluster at 780px (ETH CVL), 800px (Hinton) and 825px (MIT CSAIL). Measured prose columns across the sample span 540px/60ch (Stanford SAIL) to 1024px/105ch (MIT HAN Lab), median 780px/86ch. 760px/91ch is inside the band and adjacent to the modal designed container. Note that the real-world modal measure (86ch) is well above the textbook 45–75ch, so **do not "correct" this toward a narrower generic ideal.**

**Rule — 760px caps anything a reader reads as sentences.** Paragraphs, list items, figure captions, headings, decks, bios. Full width (1120px, `--page`) is permitted in exactly three cases and no others:

1. **Rules and dividers.** A section rule may span the full shell over inset content. This is the existing convention and is the benchmark pattern.
2. **Grid containers whose own columns are each ≤760px.** The two-column `.member-grid` spans 1120px with 536px columns — allowed.
3. **Single- or two-line bibliographic records.** `/publications/` entries. Records are not prose. HAN Lab runs citations at 1024px, zlab.bio at 1079px.

Anything that wraps to three or more lines is prose and must be capped. That decides every current exception: `.member__bio` (5 lines) caps; `.opp-cta` (prose) caps; `.pub` entries (1–2 lines) do not; `.page-head h1` caps — change `baseof.html:114` from `max-width: 900px` to `max-width: var(--measure)`.

Delete the `.measure { max-width: var(--measure) }` utility at `baseof.html:78` or start using it; it is currently applied to nothing.

### 3.4 One label column

**76px column, 24px gutter, text at x=260 on every list on the site.**

76px is the existing `.member` value and is on the 4px grid (4×19). 24px is `--s-5`; the current 20px is not on the scale.

The PI keeps `grid-column: 1 / -1` — a full-row span is how HAN Lab distinguishes its PI and it costs no alignment — but drops to the same 76px portrait track. Delete `grid-template-columns: 104px minmax(0,1fr)` from `layouts/people/list.html:10` and the `.member--pi .member__portrait { width: 104px; height: 104px }` override. Add `.member__bio { max-width: var(--measure) }`.

An objection was raised that capping the PI bio at 760px leaves the block 236px short of the section rule above it. That objection does not survive: student bios already stop at 696px, 584px short of the same 1280px rule, and the entire point of a measure is that text stops short of the container. Cap it.

The five dead label-column widths (180 / 110 / 130 / 230 / 280px) go with the dead CSS in §5 P2.

### 3.5 Figure alignment

Three rules.

**(a) Ink aligns, not boxes.** A figure's leftmost *drawn* pixel sits on the text column's left edge. Implement by tightening every SVG's `viewBox` to its measured ink bounding box plus a uniform 8-unit pad on all four sides. Current dead canvas runs 17.7%–30.8% per file with left/right asymmetries up to 2.9× and top/bottom up to 4.1×.

When tightening a `viewBox`, three values must change in lockstep or nothing happens: the `viewBox`, the SVG root's `width`/`height`, and the `width`/`height` attributes on the `<img>` in the layout. A `viewBox`-only edit leaves the intrinsic size unchanged and `preserveAspectRatio="xMidYMid meet"` letterboxes the same whitespace back in.

**(b) Figures may exceed the measure; captions may not.** A schematic is not prose, so a figure may run to 1120px. Its `<figcaption>` is capped at 760px and shares the figure's left edge. Caption sits `--s-2` (8px) below the image box; after (a), that is also the visible gap.

**(c) Legibility floor — this is the rule that was missing and that let the 260px regression ship.**

> The smallest text in any diagram must render at **≥11 CSS px at the narrowest width at which the file is served.**
> `effective_px = svg_font_size × (display_width ÷ viewBox_width)`

11px is derived from: the site's own smallest live type is 12px; Nature's 5pt floor at 88mm single-column corresponds to roughly 11.4px at typical web raster; and the benchmark's own self-drawn diagram (MIT HAN Lab) renders its labels at ~14.8px effective. Anything below 11px is texture, not information.

Corollary, computed: at a 260px display from a 560-unit `viewBox` (scale 0.464) the minimum authored font-size is 23.7 units. Nothing in the four direction files exceeds 16. So the thumbnails must be **redrawn on a canvas authored at the served size** (~260×195 viewBox, type at 11–13 units, 1:1) rather than resized. See §4.

A diagram whose content is more than half text and which cannot meet the floor at its served width is not served at that width. Add to `ADMIN_GUIDE.md`: after adding any figure, screenshot the page at 1440 and 375 and look at it.

### 3.6 Uppercase tracking

```css
--caps-track: 0.08em;
```

Applied to every `text-transform: uppercase` rule. At `--t-1` on a 10px context (`.brand__meta`) use `0.10em`.

Benchmark: 14 of 14 tracked instances, +0.045em to +0.083em. 0.08em is at the top of that band, which suits Arial's relatively open caps. Implementing it as a token rather than ten literals is the point — the literal-per-rule approach is exactly how v2 lost the tracking that v1 had.

Also apply the `.kicker` specificity fix in the same edit, since it is the same block of rules:

```css
.page-head .kicker, .home-intro .kicker, .kicker {
  margin: 0 0 var(--s-4);
  color: var(--claret);
  font-size: var(--t-1);
  font-weight: 700;
  letter-spacing: var(--caps-track);
  text-transform: uppercase;
}
```

Add the equivalent override inside the ≤700px media queries at `baseof.html:234` and `index.html:39`, and verify across all 39 kicker-bearing pages, not the 7 originally sampled.

### 3.7 Fonts — keep Georgia and Arial, spend nothing

**Recommendation: no change. Do not buy, self-host or switch a typeface.**

The evidence against Georgia is real and I will state it plainly. Across 30 page loads on 12 top-lab sites I enumerated every first-choice family that actually renders text: 19 families — `-apple-system`, Anaheim, Arial, DINPro, Exo, Helvetica Neue, Inter, Material Icons, Muli, Open Sans, Poppins, SFMono, Source Sans Pro, basis-grotesque ×3, `sans-serif`, `system-ui`. **Zero serif.** Not one of the twelve, including the austere ones (Karpathy, PDOS, Hinton) and the plain ones (zlab.bio on stock Squarespace), uses a serif for body or headings. Georgia display over an Arial body has no precedent in the peer group.

The evidence for keeping it:

1. **Shipping no webfont is normal and evidenced.** 5 of 12 ship none: zlab.bio (`loadedFaces=[]`, renders Arial for 21 text elements and Helvetica Neue for 14 including its h2), THUNLP, MIT PDOS, karpathy.ai, and Hinton (declares Inter, ships no `@font-face`). One of the highest-profile labs in biology renders its body prose in plain Arial. The PI's own survey §1.3 concluded the same thing from a larger sample.
2. **The cost is not just the file.** Two weights of a grotesque is ~50–80 KB woff2, a build step, a FOUT/FOIT decision and CLS risk on a site that currently has none. More seriously, it would break the diagrams: an SVG referenced through `<img>` cannot load a webfont, so the five schematics would keep rendering Arial while the page rendered the new face — a new inconsistency created to fix an old one.
3. **The panel-lens read filed serif headings as a strength**, contributing to a register of restraint. Georgia is dated, not sloppy. The measurable failures — untracked capitals, 30 sizes, no measure discipline — cost more and cost nothing to fix.

**If a future decision overrides this**, the benchmark route is one grotesque family at two or three weights (CSAIL uses basis-grotesque regular/medium/bold; Stanford uses Poppins 600/700). Seven of seven webfont adopters use a single family across body and headings. **None pairs a webfont with a system serif.** Do not add a second family to the two that already exist.

Also correct the calibration source: `cwanglab_website_review.md:32` states that Hinton's page is hand-written black-on-white HTML. Re-measured 28 July 2026, it is a three-column Bootstrap card grid on a blue-grey background loading bootstrap-icons from cdnjs, h1 24px/w500, 4 distinct sizes. The survey's conclusion still holds — it ships no webfont — but the specific claim should not be quoted. Karpathy remains a valid hand-written-HTML example.

### 3.8 What is already correct — do not touch

- Flush-left everywhere. 497/497 nodes `text-align: start`; homepage returns `{'start': 20}` and `/research/` `{'start': 12}`. Benchmark: 9 of 10 pages flush-left, the sole exception being HAN Lab. **Never add `text-align: justify`.**
- Heading-to-prose left-edge pairing: 12/12 aligned within 2px across the homepage and `/research/`, against a benchmark of 29/32 (91%). This is the single largest reason the site reads as ordered.
- 760px measure and 17px body (§3.1, §3.3).
- Zero-dependency inline CSS; byte-identical geometry at 1280 and 1440; the 1000px nav breakpoint at `baseof.html:217`, which was a deliberate fix and holds.
- One low-saturation accent (`--claret: #7a1732`) on white, no gradients, no motion beyond a reduced-motion-guarded transition.

Add a regression guard: the heading/prose left-edge pair check is scriptable. Port it into `scripts/` and run it against localhost before any layout change lands.

---

## 4. Figures

### 4.1 What is good, and must survive any reorganisation

**Crediting is stricter than all 16 benchmark sites.** `layouts/research/single.html:37-41` renders a `<figcaption>` plus a "Source: *label*" hyperlink, and `content/research/medical-imaging.md:14` supplies "Xu et al., Nature Communications" with a live DOI (10.1038/s41467-024-55422-4, Crossref-verified, PI a co-author, CC-BY). Against that: MIT HAN Lab serves paper screenshots with `alt=""` and no credit; ETH CVG serves all 15 teasers with `alt="img"`; zlab.bio serves files named `Screenshot 2025-12-18 at 3.16.30 PM.png`.

Alt text is descriptive and specific. Captions are prefixed "Schematic." so a drawing cannot be mistaken for a result. `content/research/medical-imaging.md:12` voluntarily discloses the QC attrition (50,226 scanned, 48,608 retained) rather than quoting the flattering number.

Palette is exact: all five SVGs draw only from `#7a1732`, `#5f6368`, `#3c4043`, `#f7f7f5`, `#d8d9da` — byte-identical to the CSS custom properties at `baseof.html:45-53`. Zero `gradient`, `filter`, `feDropShadow` or `feGaussianBlur` elements in any file. Total weight of all five diagrams is 26,566 bytes.

### 4.2 Defects, with measured numbers

**F1 — Four homepage thumbnails are illegible. (P1)**
`layouts/index.html:33` sets `.dir-item .dir-thumb { flex: 0 0 260px; width: 260px }` against a 560-unit `viewBox`: scale 0.4643.

| File | smallest authored | renders at | largest authored | renders at |
|---|---|---|---|---|
| `dir-robotics.svg` | 9.5 | **4.41px** | 16 | 7.43px |
| `dir-heterogeneous.svg` | 10 | 4.64px | 15.5 | 7.20px |
| `dir-terminal.svg` | 10 | 4.64px | 16 | 7.43px |
| `dir-medical-ai.svg` | 10 | 4.64px | 13 | 6.03px |

Body text alongside is 17px. Cropped at 3× nearest-neighbour from a 1:1 screenshot, "local model: ResNet", "data stays local", "model updates only" and "cloud-side aggregation" have no resolvable glyphs. The topology survives; the annotation layer is lost entirely.

Note two things this is *not*. It is not a case for deleting the images: the PI's own survey asks for research schematics as visual anchors (`cwanglab_website_review.md:105`) and criticises a text-only hero (line 69). And it is not a case for enlarging in place: the text column beside them is currently 52–60ch, which is correct, and widening it to 738px would put it at 86–90ch.

**Fix: redraw all four on a 260×195 canvas at 1:1, with at most five labels each at font-size ≥11.** Delete the sub-13-unit annotations rather than shrinking the drawing to fit them.

**F2 — `framework.svg` is illegible on mobile. (P1)**
Served at 1080px desktop from a 1400-unit `viewBox` (0.771): sizes 26/21/17/13.5/12.5/12/11.5 render at 20.06 / 16.20 / 13.11 / 10.41 / 9.64 / 9.26 / **8.87px**. Readable but below the §3.5(c) floor at the bottom end. At a measured 500px viewport (0.334): 3.84–8.69px — even the CLOUD / EDGE / TERMINAL headings render at 8.69px. At a real 375px phone the shell is ~343px, scale 0.245, i.e. 2.8–6.4px.

Fix: (a) raise the file's floor from 11.5 to 15 units so its desktop minimum is 11.6px — which means deleting the three redundant italic footers (see F6); (b) hide `.framework-figure` below the 700px breakpoint. The three prose bullets at `index.html:72-74` already state Cloud / Edge / Terminal, so nothing is lost. Hiding is the correct answer; a stacked mobile variant is optional later work.

**F3 — `dir-medical-ai.svg` breaks the set. (P1)**
`viewBox="0 62 560 205"` (2.73:1) against three siblings at `"0 0 560 420"` (1.33:1). Rendered: 600×220 on its research page against 600×450 for the others; 260×95.2 against 260×195 on the homepage. It is also the only one of the four that is a numbered linear pipeline; the others are hub-and-spoke.

Compounding it, `layouts/index.html:107` hard-codes `width="480" height="360"` for **all four** thumbnails. Correct for three, wrong by 2.7× for this one. Above 700px the rows are text-driven so nothing shifts; below the breakpoint `.dir-item` becomes `display:block`, the placeholder reserves 260×195 and collapses to 260×95 on load — a ~100px layout shift, made later and more visible by `loading="lazy"`.

Fix rides with F1: redraw on the same 260×195 canvas as its siblings, and add per-figure `w`/`h` keys to the `$dirFig` dict at `index.html:86-91`.

**F4 — The caption describes a different figure. (P0)**
`content/research/medical-imaging.md:7-8`:
> `diagram_alt: "Overview of trustworthy medical AI: imaging measurements that stay reliable across scanners, hospitals and patient groups"`

The drawing is: Whole-body MRI → deep-learning measurement → phenome-wide and genome-wide association (PheWAS · GWAS) → clinical insights. Nothing in it depicts scanners, hospitals or patient groups varying. The file's own `aria-label` (line 1) reads "Whole-body MRI measurement and association pipeline" — accurate to the drawing and in direct conflict with the caption the page supplies.

This is a substantive error, not a styling one, and it is wrong for screen-reader users. Fix: rewrite the caption to describe the pipeline that is drawn. Five minutes.

**F5 — The two deployed paper figures are under-resolved. (P2)**
`bone-marrow-measurement.png`: natural 800×305, rendered 800.0×305.0 → **1.000×**. `soft-robot-sensorimotor.png`: natural 920×485, rendered 800.0×421.7 → **1.150×**. Both are forced to the container width by `layouts/research/single.html:7-8`, so neither can fall back to its natural size. On any 2× display the bone-marrow figure is upscaled 2:1. Compare: the site's own logo runs 6.59×; MIT HAN Lab serves research figures at 2.95–4.80×; MMLab@NTU at 1.83–2.94×.

Source is available and licensed: Nature Communications Fig 1 at 1758×2048 under CC-BY 4.0 for DOI 10.1038/s41467-024-55422-4; panel A is the exact crop already deployed. Re-cropping at full resolution gives 2.20× into the same 800px slot with no CSS change.

Honest caveat: a higher-resolution re-export will not fix legibility inside `soft-robot-sensorimotor.png`. The label "Motor nerve signals" measures 87 native px for 19 characters, i.e. roughly 7 CSS px effective at the 800px display width. It will still be too small. That figure needs a tighter panel crop, not just more pixels.

**F6 — `framework.svg` says the same thing four times per box. (P2)**
CLOUD box: heading (line 12), subtitle (14–15), two bullets (17, 19), italic footer (20) which paraphrases the bullets. Same in EDGE (34 paraphrases 30 and 32) and TERMINAL (48 paraphrases 45 and 47). The EDGE box additionally carries four distinct type sizes (26 / 17 / 13.5 / 11.5), the 11.5 being a single stray string "(data stays local)" left-aligned at x=566 while the box's other italic is centred at x=700 — and it is already stated by line 34 and by `index.html:73`.

Delete lines 20, 34 and 48. That reclaims ~42 units of height, raises the file's type floor, and pairs with the F2 fix and the viewBox tightening.

`dir-robotics.svg` has the parallel problem: three left-hand boxes all 165×70 units carrying 4, 2 and 1 text lines respectively, with the left column left-aligned at x=76 while the hub and application boxes are centred — two alignment regimes in one figure.

**F7 — Three paper figures are orphaned; two research pages show only boxes. (P1)**
`static/images/research/` contains `bone-marrow-study-design.png` (344,024 B), `federated-heterogeneous-distillation.png` (75,893 B) and `selora-adaptation.png` (29,245 B). Grep across the built tree returns zero references to any of them. Meanwhile `/research/heterogeneous-learning/` and `/research/efficient-models/` each render exactly two images — the logo and a schematic — and no result.

Two of the three are botched crops. `selora-adaptation.png` (760×175) has a partial line of the source paper's own caption sliced through its bottom edge: "Fig. 1: Training illustration of … SeLoRA …". `federated-heterogeneous-distillation.png` (990×190) has "(a) cloud-to-fog distillation" and "(b) fog-to-cloud distillation" clipped through the letterforms. Measured bottom ink margin: 0px on both.

Fix: re-crop from the source PDF on a clean panel boundary at ≥2× display width, then wire in via the `image:` / `image_alt:` / `image_caption:` / `image_source_label:` / `image_source_url:` front matter that `layouts/research/single.html:35-41` already handles. Do not deploy the current crops.

**F8 — Zero photographs; 11 cartoon avatars still shipped. (P0 for the deletion, P3 for the photographs)**
`static/avatars/` holds 11 SVGs whose embedded metadata reads `<dc:title>Notionists</dc:title><dc:creator>Zoish</dc:creator>` — CC0 cartoon faces from the DiceBear set. Referenced zero times in `content/`, `layouts/` and `data/`, absent from the 45-URL sitemap, but built and reachable: `/avatars/pi.svg` returns HTTP 200. These are the same files that, in v1, depicted the PI as a cartoon and Assoc. Prof. Marta Vallejo as a man in a necktie. `git rm` them so they cannot be wired up by a future edit — note that `cwanglab_website_review.md:98` reads "接线已备好的头像资源" (wire up the prepared avatar resources), which is presumably why v1 did it, and which must not be cited again.

Ten of sixteen benchmark labs lead with a photograph of people or the lab. The five that show none show almost no imagery at all (BAIR: 1 image, the logo; PDOS: 1; Cambridge MLG: 0). What has no precedent in the sample is imagery consisting mainly of self-drawn schematics, which is what this site currently is: a site-wide grep of the built HTML yields 9 distinct image files — the logo, five self-drawn SVGs, two paper figures and one admin-page logo.

The monogram circles on `/people/` should stay. They were introduced by commit `148e11b` specifically to replace the cartoons, they are `#f7f7f5` fill with a `#d8d9da` ring and Georgia claret letters (a bookplate monogram, not a SaaS avatar chip), and the page states the consent policy in its intro. Removing the monogram span alone leaves 16 empty grey rings that read as broken images, because `.member__portrait` keeps its 76px box, border and background. Leave them; fill them with photographs when consent returns.

**F9 — The header logo. (P2)**
`static/images/logo-claret.png` is 356×356 RGB, rendered at 54×54 by `baseof.html:304`. The source carries a 1px claret perimeter keyline which downscales to `(231,214,218)` against the `#ffffff` header — a faintly visible pale-pink box, confirmed by A/B: cropping 2px off the source removes it while leaving the interior fill (254,254,254, imperceptible against white) unchanged. The baked-in wordmark occupies rows 256–296 and renders at 2.3–2.7px cap height, i.e. an illegible smear that also duplicates the `.brand__name` text 13px to its right. Because of it, the actual glyph occupies 186 of 356 px — 52% — so the mark renders at roughly 28px in a 54px slot.

Fix: export a symbol-only, keyline-free, transparent-background variant of the glyph and point `baseof.html:304` at it. That recovers the wasted 48% and removes the box in one change. Keep the full lockup for `og-image.png` only. While there, correct `static/favicon.svg:1`, whose `aria-label` still reads "C. Wang Research Group".

**F10 — Cosmetic, one-line each. (P3)**
`framework.svg` lines 12, 26, 40 use `text-anchor="middle"` with `letter-spacing="3"`; SVG applies the tracking after the final glyph, so the ink centre of CLOUD, EDGE and TERMINAL sits 1.50 units (1.16 CSS px) left of the box centre. Add `dx="1.5"`. `dir-medical-ai.svg:47` has "phenome-wide and" at 106.3 units advance inside a 118-unit box — 5.8 units clearance each side; widen the rect to 130.

`index.html:68` carries `loading="lazy"` on `framework.svg`, which is near the top of the homepage. Remove it.

### 4.3 Toolchain — which tools, decisively

| Figure type | Tool | Why |
|---|---|---|
| Conceptual schematic (the five diagrams) | **Hand-authored SVG**, edited directly or in **Inkscape + Scientific Inkscape** | It is the delivery format with no export step; it diffs in git; text stays real `<text>` so it is selectable, accessible and resolution-independent; 4.7–5.9 KB per file against HAN Lab's 63–126 KB PNG exports. Scientific Inkscape's Homogenizer "set[s] all fonts, font sizes, and stroke widths in a selection to common values" — it mechanically performs the §3 remediation. Its Scaler resizes a drawing without touching its text. |
| Result figure from a published paper | **No design tool.** `pdftoppm -r 300 -png` from the publisher PDF, then a tight panel crop | Both source papers are CC-BY. This is a raster export step, not a design task. Credit with the existing `image_source_label` / `image_source_url` pattern. |
| Plot or chart from data | matplotlib / R → SVG → Inkscape Homogenizer | Same reason as the schematics; keeps the committed SVG as source of truth. This is the stack the Holden Lab (Warwick) recommends for scientific illustration. |
| Photographs | **No tool.** `CONSENT_EMAIL.md` | Generated or cartoon faces on an academic People page are worse than a blank space. This is the one place where reaching for an image tool is actively harmful. |
| Sketching before drawing | `figma-generate-diagram` / FigJam, **internal only** | Acceptable as a thinking surface. Never as a shipped asset: its own `SKILL.md:26-29` states it cannot change fonts, cannot move individual shapes and cannot be edited node-by-node after generation, and FigJam defaults to Inter. |

**Do not use, and why:**

- **`frontend-design`** (any installed copy). `SKILL.md:36` — "NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, **Arial**, system fonts)"; `:34` — "gradient meshes, noise textures, dramatic shadows, decorative borders, custom cursors, and grain overlays"; `:13` — "commit to a BOLD aesthetic direction"; `:33` — "Asymmetry. Overlap. Diagonal flow. Grid-breaking elements." Against `specs/003-academic-visual-system.md:5` ("system serif and sans-serif stacks") and `:7` ("no gradients, decorative blobs, animation, hover lift, oversized marketing hero or nested cards"). Two unique versions are installed across nine on-disk copies (md5 `31c6336…` ×5, `5c39256…` ×4), so which doctrine would apply is not even predictable.
- **`canvas-design`** — `SKILL.md:7` outputs only `.md`, `.pdf` and `.png`; `:79` mandates "MINIMAL TEXT"; `:82` "ART OBJECTS, not documents with decoration". Wrong format and the opposite brief from a labelled schematic.
- **`brand-guidelines`** — `SKILL.md:21-30` applies Anthropic's palette (`#d97757`, `#6a9bcc`) and Poppins/Lora. A different organisation's brand on a Heriot-Watt site.
- **`theme-factory`** — ten slide-deck themes ("Ocean Depths", "Midnight Galaxy").
- **`algorithmic-art`** — p5.js `.html` and `.js`.
- **`web-artifacts-builder`** — React + Tailwind + shadcn bundled to a claude.ai artifact.
- **Canva MCP, and Figma for shipped assets.** Figma MCP is live on this machine but the account is a personal Gmail (`wangchengjia1986@gmail.com`) on Starter tier — a 3-file team cap and 30 days of version history, which is thin for a long-lived asset. Its SVG export also needs cleanup before it is fit to inline.

Record this exclusion in `CLAUDE.md` or `.claude/`, **not** in `specs/003`, which describes site behaviour rather than build-agent policy.

### 4.4 Which publisher standards actually apply

Be precise here, because one source audit over-applied them. Nature's *Guide to Preparing Final Artwork* governs **print submissions at fixed column widths** (88mm single, 180mm double). It is not the governing standard for a web schematic, and the site's diagrams neither pass nor fail it in any meaningful sense — measured, `framework.svg` at 180mm spans 4.19–9.48pt and the direction files at 88mm span 4.23–7.13pt, outside the 5–7pt window at both ends. Quoting that as a failure would be a category error.

Three things do transfer:

1. **Sans-serif, Helvetica or Arial preferred** (Nature, p.1). 73 of 87 `font-family` declarations across the five SVGs are already `Arial, Helvetica, sans-serif`. The remaining 14 are `Georgia, 'Times New Roman', serif` and carry the most prominent text in every figure. Given §3.7 keeps Georgia for site headings, this is a deliberate inconsistency with Nature's rule and an acceptable one — the figures are web assets matching the site, not manuscript submissions. Do not "fix" it by adding `@font-face`; an SVG referenced through `<img>` cannot load one.
2. **No drop shadow, 3D or bevel** (Nature, p.2). Already fully compliant.
3. **Bitmaps at 300dpi** (Nature); eLife requires "a minimum dpi of 300 and a minimum physical width size of 10cm". This is the standard the two deployed PNG crops fail, and it is the reason F5 is worth the hour.

The operative rule for this site is §3.5(c): **≥11 CSS px at the narrowest served width.** It is the web translation of the print floor, it is checkable with one line of arithmetic, and it is the rule whose absence let the 260px thumbnails ship.

---

## 5. Prioritised plan

Ordered by credibility gained per hour. "PI?" marks whether the item can be implemented without Dr Wang.

### P0 — costs credibility now, cheap to fix

| # | Change | File(s) | Effort | Buys | PI? |
|---|---|---|---|---|---|
| 1 | Delete the 11 DiceBear cartoon SVGs, live at HTTP 200 | `git rm static/avatars/` | 2 min | Removes caricatures of two named professors from production | No |
| 2 | Fix the caption/alt that describes a different figure | `content/research/medical-imaging.md:7-8` | 5 min | Removes a substantive error on the flagship research page | No |
| 3 | Repoint or remove the footer GitHub link | `data/site.yaml:12`, `baseof.html:352` | 5 min | Stops sending readers to a "Full-stack developer" profile with dotfiles and a Coolify fork | Removal: no. Fixing the account bio: **yes** |
| 4 | Correct the soft-robot preprint title to the Crossref string ("**enables**", en dash in "tactile–morphological") | `content/research/intelligent-systems.md` | 5 min | The only paper cited as representative work in a whole direction | No |
| 5 | Delete or re-crop the two orphan PNGs with paper captions sliced through them | `static/images/research/` | 10 min | Removes a latent trap; nobody can wire in a botched crop later | No |
| 6 | Add the ISBI 2026 paper (PI corresponding author, Mao and Pan co-authors) | new `content/publications/isbi-sam-distillation-2026.md` from `CV/citations.bib:40-43` | 30 min | Closes the most conspicuous gap in the publications archive | No |
| 7 | Tighten `dir-medical-ai.svg:18` from a bare "50,226 participants" to a scoped label | `static/images/diagrams/dir-medical-ai.svg` | 5 min | The one participant-count surface with no qualifier. **Do not touch the homepage's "around 47,000" — it is correct** | No |

### P1 — visible craft, minutes to a day

| # | Change | File(s) | Effort | Buys | PI? |
|---|---|---|---|---|---|
| 8 | `--caps-track: 0.08em` token, applied to all 11 uppercase rules | `baseof.html`, `projects/single.html:5`, `publication-single.html:13` | 20 min | Closes the most consistent benchmark violation (14/14 tracked in sample) and reverses a regression from v1 | No |
| 9 | `.kicker` specificity + size fix, desktop and both mobile queries | `baseof.html:98,234`, `index.html:39` | 20 min | 39 pages get the 13px claret eyebrow the author intended; kills the widowed "UNIVERSITY" | No |
| 10 | `/people/`: PI to a 76px label column, `.member__bio` capped at `--measure` | `people/list.html:9,10` | 15 min | Removes the 28px stair-step at the PI/student boundary and the 69ch→135ch jump on the most-read page | No |
| 11 | `.page-head h1` `max-width: 900px` → `var(--measure)` | `baseof.html:114` | 2 min | Removes the second right rail on the eight long-titled detail pages readers arrive at from DOIs | No |
| 12 | `/opportunities/`: h2 flush at 160, one list indent, `.opp-cta` capped | `opportunities/list.html:5,17,20,21` | 20 min | Four left edges → one on the page a prospective PhD student reads end to end | No |
| 13 | `canonifyURLs = false` | `hugo.toml:5` | 2 min | Local previews stop fetching assets from production, so screenshot review is faithful | No |
| 14 | Homepage h1: replace the duplicated lab name with the research claim | `index.html:51` | 10 min | Recovers the strongest typographic slot on the site, currently spent restating the masthead 90px below it | Wording: **yes** |
| 15 | Redraw the four direction thumbnails at 260×195, 1:1, ≤5 labels each at ≥11 units; per-figure `w`/`h` in `$dirFig` | 4 SVGs, `index.html:86-91,107` | 1 day | Removes four illegible objects from the homepage and the ~100px mobile CLS | No |
| 16 | Re-crop and wire in the two orphan paper figures | `content/research/heterogeneous-learning.md`, `efficient-models.md` | 3 h | Two of four research directions currently show a box diagram and no result | No |

### P2 — systemic; invisible individually, compounding

| # | Change | File(s) | Effort | Buys | PI? |
|---|---|---|---|---|---|
| 17 | Type + spacing token ladder (§3.1, §3.2); replace 30 font-size and 38 spacing literals | all 11 layout `<style>` blocks | 1 day | Removes the substrate under every other alignment finding; pins leading to two ratios | No |
| 18 | Delete the 107 dead rule blocks (47 classes) | `baseof.html:97-205` | 2 h | Provably pixel-identical render; removes 1.4 KB gzipped/page and the five phantom label-column widths | No |
| 19 | Re-export both deployed paper figures at ≥1600px from the CC-BY sources | `static/images/research/` | 2 h | The group's flagship result stops being visibly resampled on the PI's own laptop | No |
| 20 | Tighten all five SVG `viewBox`es to ink + 8-unit pad; delete `framework.svg`'s three italic footers; hide the framework figure below 700px; remove `loading="lazy"` | 5 SVGs, `index.html:25,68` | 4 h | Fixes the 54.6px caption gap, the 2.9× and 4.1× margin asymmetries, and mobile illegibility | No |
| 21 | Symbol-only logo variant, keyline and wordmark removed; fix `favicon.svg` aria-label | `static/images/`, `baseof.html:304`, `static/favicon.svg:1` | 2 h | Removes the pale-pink box on every page and recovers 48% of the header slot | No |
| 22 | Write `specs/005-figure-spec.md` (§3.5 rules) and the skill-exclusion note in `CLAUDE.md` | new files | 2 h | Stops the 260px class of regression recurring | No |
| 23 | Delete the legacy `.news-item` grid and the defensive `.news-feed` prefix | `baseof.html:196`, `news/list.html` | 15 min | Removes the one live specificity war | No |

### P3 — content; mostly needs the PI, and this is where the remaining points are

| # | Change | File(s) | Effort | Buys | PI? |
|---|---|---|---|---|---|
| 24 | **One group photograph** at ~1100px on `/people/` | `static/images/people/`, `content/people/` | multi-day | The only hard standard all 35+ surveyed labs meet, and the one both generations score zero on. Higher value than every item above it | **Yes** |
| 25 | Move "Selected publications" above "People" on the homepage; give each Nature Comms line a **finding**, not a method; link the journal name to the DOI | `index.html:53` and section order | 3 h | The single change with the largest effect on what a three-minute reader takes away | Wording: **yes** |
| 26 | Add the two doctoral alumni destinations — both are already public on `vios.science/team` (Xia → postdoc, Edinburgh; Chartsias → Ultromics) | `content/people/tian-xia.md`, `agisilaos-chartsias.md` | 30 min | Closes hard standard 2 for the two people it actually governs | Courtesy email advisable |
| 27 | Rename "Doctoral alumni" → "Co-advised doctoral researchers" and label the dates as co-advising windows | `content/people/` | 15 min | Removes a credit ambiguity in front of the exact community that knows the provenance | No |
| 28 | Backfill news to roughly quarterly (ISBI April, PR papers June, preprint December) and widen beyond category "Publication" | `content/news/` | 3 h | Current gaps are 367 / 264 / 255 days against a ~92-day standard | Partly |
| 29 | A sourced record block on `/about/`: US patent 9275432, OPTIMAT Co-I £677,094, named trials with **CV-verbatim** roles | `content/about/_index.md` | 3 h | v2 removed v1's inflated numbers, correctly, and then swung past the mark — a reader cannot tell a two-year-old group from an eighty-paper record. **State nothing that cannot be pointed at a line in `c_cv2.tex`** | **Yes** |
| 30 | `oa_url` or accepted manuscript for the three paywalled entries (both Pattern Recognition, one Comput. Biol. Med.) | `content/publications/` | 2 h | The two most recent journal papers are the worst subset to paywall | Repository access |
| 31 | Restore a concrete recruiting statement if one is true, and port v1's Join prose | `content/opportunities/` | 2 h | The highest-converting page on the site currently advertises nothing, and the two generations contradict each other on whether the group is recruiting | **Yes** |
| 32 | Collect alumni destinations for the 20 taught/intern roster entries; add a year range to Yuchen Mao (first author of SeLoRA and ISBI 2026, currently rendered as name + "Research Intern") | `CONSENT_EMAIL.md`, `content/people/` | multi-day | Turns a headcount into a training record | **Yes** |
| 33 | Correct the IEEE TMI entry in the CV — the site has it right and the CV has it wrong: Crossref 10.1109/tmi.2020.3036584 is "Disentangle, Align and Fuse for Multimodal and Semi-Supervised Image Segmentation", issued 2021-03, not "…zero-shot…", 2020 | `CV/c_cv2.tex:195`, `CV/citations.bib:130` | 10 min | Not a website item, but it is an error in the authoritative source | No |

### Not to be done

- **Do not change the homepage's "around 47,000".** Refuted; it matches the paper's abstract verbatim and commit 771c850 already corrected it *to* this value once.
- **Do not delete the four homepage thumbnails.** Redraw them. Deleting contradicts the PI's own survey and widens the adjacent text column past 80 characters.
- **Do not cap `/publications/` entries at 760px.** They are bibliographic records, not prose; HAN Lab and zlab.bio run theirs wider.
- **Do not "fix" the 45px framework figure inset in isolation.** Symmetric figure margins are the benchmark norm; it resolves as a side effect of P2 #20.
- **Do not buy, self-host or switch a typeface.** §3.7.
- **Do not remove the `/people/` monograms.** Fill them.
- **Do not port anything from v1's metrics readout, funding figures, trial list or avatar system.** §1.
