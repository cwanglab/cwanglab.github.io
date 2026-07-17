#!/usr/bin/env python3
"""Discover and verify papers without publishing social posts."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

USER_AGENT = "cwanglab-paper-watch/1.0 (mailto:Chengjia.Wang@hw.ac.uk)"


def request_json(url: str, headers: dict[str, str] | None = None) -> dict:
    request_headers = {"Accept": "application/json", "User-Agent": USER_AGENT}
    request_headers.update(headers or {})
    request = urllib.request.Request(url, headers=request_headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} for {url}: {detail[:300]}") from exc


def normalise_doi(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^https?://(dx\.)?doi\.org/", "", value, flags=re.I)
    return value.lower()


def strip_markup(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def crossref_record(doi: str) -> dict:
    encoded = urllib.parse.quote(normalise_doi(doi), safe="")
    message = request_json(f"https://api.crossref.org/works/{encoded}")["message"]
    authors = []
    for author in message.get("author", []):
        name = " ".join(part for part in [author.get("given"), author.get("family")] if part)
        if name:
            authors.append(name)
    return {
        "doi": message.get("DOI", normalise_doi(doi)),
        "title": (message.get("title") or [""])[0],
        "authors": authors,
        "venue": (message.get("container-title") or [""])[0],
        "type": message.get("type", ""),
        "published": message.get("published", {}).get("date-parts", [[None]])[0],
        "abstract": strip_markup(message.get("abstract")),
        "publisher_url": message.get("URL", f"https://doi.org/{normalise_doi(doi)}"),
    }


def unpaywall_record(doi: str, email_address: str) -> dict:
    encoded = urllib.parse.quote(normalise_doi(doi), safe="")
    email_query = urllib.parse.urlencode({"email": email_address})
    result = request_json(f"https://api.unpaywall.org/v2/{encoded}?{email_query}")
    best = result.get("best_oa_location") or {}
    return {
        "is_open_access": result.get("is_oa", False),
        "oa_status": result.get("oa_status", ""),
        "landing_page": best.get("url_for_landing_page", ""),
        "pdf_url": best.get("url_for_pdf", ""),
        "license": best.get("license", ""),
        "version": best.get("version", ""),
    }


def discover_openalex(author_id: str, from_date: str, until_date: str | None) -> list[dict]:
    api_key = os.environ.get("OPENALEX_API_KEY")
    if not api_key:
        raise RuntimeError("Set OPENALEX_API_KEY to use OpenAlex discovery.")
    author_id = author_id.rsplit("/", 1)[-1]
    filters = [f"authorships.author.id:{author_id}", f"from_created_date:{from_date}"]
    if until_date:
        filters.append(f"to_created_date:{until_date}")
    params = urllib.parse.urlencode({
        "filter": ",".join(filters),
        "sort": "created_date:desc",
        "per-page": 100,
        "select": "id,doi,title,display_name,publication_year,publication_date,type,primary_location,authorships,created_date,updated_date,is_retracted",
        "api_key": api_key,
    })
    data = request_json(f"https://api.openalex.org/works?{params}")
    return data.get("results", [])


def write_json(data: object, output: str | None) -> None:
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if output:
        Path(output).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:72] or "paper"


def make_social_draft(doi: str, output_dir: str, email_address: str | None) -> Path:
    crossref = crossref_record(doi)
    oa = unpaywall_record(doi, email_address) if email_address else {}
    today = dt.date.today().isoformat()
    title = crossref["title"]
    path = Path(output_dir) / f"{today}-{slugify(title)}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    fact_lines = [
        "## Verified metadata",
        "",
        f"- DOI: https://doi.org/{crossref['doi']}",
        f"- Venue: {crossref['venue'] or 'Check required'}",
        f"- Authors: {', '.join(crossref['authors']) or 'Check required'}",
        f"- Open access: {oa.get('is_open_access', 'Not checked')}",
        f"- Open-access location: {oa.get('landing_page') or 'None recorded'}",
        "",
        "## Review notes",
        "",
        "Confirm publication status, author order, central claim, funding, account tags, image rights and embargo before approval.",
    ]
    frontmatter = [
        "---",
        f"title: {yaml_string(title)}",
        f"platform_date: {today}",
        'source_record: ""',
        f"doi: {yaml_string('https://doi.org/' + crossref['doi'])}",
        'status: "draft"',
        'x_copy: ""',
        'linkedin_copy: ""',
        'website_news_title: ""',
        'website_news_summary: ""',
        'reviewer: ""',
        'review_date: ""',
        "claims_checked: false",
        "image_rights_checked: false",
        "embargo_checked: false",
        'buffer_post_ids: ""',
        'published_urls: ""',
        "---",
        "",
    ]
    path.write_text("\n".join(frontmatter + fact_lines) + "\n", encoding="utf-8")
    return path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    discover = subparsers.add_parser("discover", help="Find works created in OpenAlex for one author")
    discover.add_argument("--author-id", required=True, help="OpenAlex author ID, for example A123456789")
    discover.add_argument("--from-date", required=True, help="ISO date, for example 2026-01-01")
    discover.add_argument("--until-date", help="Optional ISO end date")
    discover.add_argument("--output", help="Write JSON to this path instead of stdout")

    verify = subparsers.add_parser("verify", help="Verify one DOI against Crossref and optionally Unpaywall")
    verify.add_argument("--doi", required=True)
    verify.add_argument("--unpaywall-email", default=os.environ.get("UNPAYWALL_EMAIL"))
    verify.add_argument("--output")

    draft = subparsers.add_parser("make-draft", help="Create a private social draft from verified DOI metadata")
    draft.add_argument("--doi", required=True)
    draft.add_argument("--output-dir", default="content/social")
    draft.add_argument("--unpaywall-email", default=os.environ.get("UNPAYWALL_EMAIL"))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "discover":
            write_json(discover_openalex(args.author_id, args.from_date, args.until_date), args.output)
        elif args.command == "verify":
            result = {"crossref": crossref_record(args.doi)}
            if args.unpaywall_email:
                result["unpaywall"] = unpaywall_record(args.doi, args.unpaywall_email)
            write_json(result, args.output)
        elif args.command == "make-draft":
            print(make_social_draft(args.doi, args.output_dir, args.unpaywall_email))
    except (RuntimeError, urllib.error.URLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

