import re
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "DwarfWikiResearchScript/1.0"}


def find_sentence(url, prefix):
    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    article = soup.find(id="mw-content-text")

    print(article is not None)

    text = article.get_text(" ", strip=True)

    # remove repeated whitespace
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)

    pattern = re.compile(
        rf"\b{re.escape(prefix)}\b.*?[.!?]",
        re.IGNORECASE,
    )

    match = pattern.search(text)

    if match:
        return match.group(1)

    return None

url = "https://dwarffortresswiki.org/index.php/Adder_man"

sentence = find_sentence(url, "Some dwarves like")

print(sentence)
