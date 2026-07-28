import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

HEADERS = {
    "User-Agent": ("DwarfWikiResearchScript/1.0 " "(personal educational project)")
}


def get_creature_urls(index_url: str) -> list[str]:
    response = requests.get(
        index_url,
        headers=HEADERS,
        timeout=20,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    creature_table = None

    for infobox in soup.select(".collapsible.infobox"):
        text = infobox.get_text(" ", strip=True)

        if "Creatures" in text and "Races" in text:
            creature_table = infobox
            break

    if creature_table is None:
        raise RuntimeError("Creature navigation table not found.")

    urls: set[str] = set()

    for link in creature_table.select("a[href]"):
        href = link.get("href")

        if not href:
            continue

        full_url = urljoin(index_url, href)

        if "/index.php/" not in full_url:
            continue

        urls.add(full_url)

    return sorted(urls)


if __name__ == "__main__":
    start_url = "https://dwarffortresswiki.org/index.php/Adder_man"

    creature_urls = get_creature_urls(start_url)

    print(f"Found {len(creature_urls)} URLs")

    for url in creature_urls[:20]:
        print(url)
