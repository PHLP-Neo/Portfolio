import re

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": ("DwarfWikiResearchScript/1.0 " "(personal educational project)")
}


def extract_matching_sentence(
    url: str,
    prefix: str,
) -> str | None:
    response = requests.get(
        url,
        headers=HEADERS,
        timeout=20,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    article = soup.find(id="mw-content-text")

    if article is None:
        raise RuntimeError(f"Article content not found: {url}")

    for unwanted in article.select("script, style, noscript, table.infobox, .navbox"):
        unwanted.decompose()

    text = article.get_text(" ", strip=True)

    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)

    pattern = re.compile(
        rf"\b{re.escape(prefix.strip())}\b.*?[.!?]",
        flags=re.IGNORECASE,
    )

    match = pattern.search(text)

    if match is None:
        return None

    return match.group(0).strip()


if __name__ == "__main__":
    test_url = "https://dwarffortresswiki.org/index.php/Adder_man"
    test_prefix = "Some dwarves like"

    sentence = extract_matching_sentence(
        test_url,
        test_prefix,
    )

    print(sentence)
