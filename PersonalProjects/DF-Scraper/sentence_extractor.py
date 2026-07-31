from __future__ import annotations

import re

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "DwarfWikiResearchScript/1.0 " 
        "(personal educational project)"
    )
}


def download_page(url: str) -> BeautifulSoup:
    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20,
    )
    response.raise_for_status()

    return BeautifulSoup(response.text, "html.parser")


def normalize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)

    return text.strip()


def extract_matching_sentence(
    url: str,
    prefix: str,
) -> str | None:
    soup = download_page(url)

    article = soup.find(id="mw-content-text")

    if article is None:
        raise RuntimeError(f"Article content not found: {url}")

    for unwanted in article.select("script, style, noscript, table.infobox, .navbox"):
        unwanted.decompose()

    text = normalize_text(article.get_text(" ", strip=True))

    escaped_prefix = re.escape(prefix.strip())

    pattern = re.compile(
        rf"\b{escaped_prefix}\b.*?[.!?]",
        flags=re.IGNORECASE,
    )

    match = pattern.search(text)

    if match is None:
        return None

    return match.group(0).strip()


def extract_raw_token(
    url: str,
    token_name: str,
) -> str | None:
    soup = download_page(url)

    raw_table = None

    for infobox in soup.select(".collapsible.infobox"):
        text = infobox.get_text("\n", strip=True)

        if "[CREATURE:" in text:
            raw_table = infobox
            break

    if raw_table is None:
        raise RuntimeError(f"RAW table not found: {url}")

    raw_text = raw_table.get_text("\n", strip=True)
    escaped_token = re.escape(token_name.strip())

    pattern = re.compile(
        rf"\[{escaped_token}:(.*?)\]",
        flags=re.IGNORECASE | re.DOTALL,
    )

    match = pattern.search(raw_text)

    if match is None:
        return None

    return match.group(1).strip()


if __name__ == "__main__":
    test_url = "https://dwarffortresswiki.org/index.php/Adder_man"

    preference = extract_matching_sentence(
        url=test_url,
        prefix="Some dwarves like",
    )

    description = extract_raw_token(
        url=test_url,
        token_name="DESCRIPTION",
    )

    print("Preference:", preference)
    print("Description:", description)
