import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://dwarffortresswiki.org/index.php/Adder_man"

headers = {
    "User-Agent": ("DwarfWikiResearchScript/1.0 " "(personal educational project)")
}

response = requests.get(
    URL,
    headers=headers,
    timeout=20,
)

response.raise_for_status()

print("Status code:", response.status_code)
print("Downloaded characters:", len(response.text))

soup = BeautifulSoup(response.text, "html.parser")

infoboxes = soup.select(".collapsible.collapsed.infobox")

print("\nInfobox count:", len(infoboxes))

# for number, infobox in enumerate(infoboxes, start=1):
#     print(f"\n--- Infobox {number} ---")
#     print(infobox.get_text(" ", strip=True)[:500])

creature_table = None

for infobox in infoboxes:
    text = infobox.get_text(" ", strip=True)

    if "Creatures" in text and "Races" in text:
        creature_table = infobox
        break

if creature_table is None:
    print("\nNo element found with id='collapsibleTable1'")
else:
    print("\nFound collapsibleTable1")
    print(creature_table.get_text(" ", strip=True)[:1000])

if creature_table is not None:
    links = creature_table.select("a[href]")

    print("\nNumber of links:", len(links))

    for link in links[:30]:
        link_text = link.get_text(" ", strip=True)
        href = link.get("href")

        full_url = urljoin(URL, href)

        print(repr(link_text), "->", full_url)