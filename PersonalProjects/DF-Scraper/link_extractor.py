from __future__ import annotations

from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup, Tag

HEADERS = {
    "User-Agent": ("DwarfWikiResearchScript/1.0 " "(personal educational project)")
}


def get_normalized_domain(url: str) -> str:
    """
    Return a normalized domain name for comparison.

    The leading 'www.' is removed so that:
    - dwarffortresswiki.org
    - www.dwarffortresswiki.org

    are treated as the same domain.
    """

    domain = urlparse(url).netloc.lower()

    if domain.startswith("www."):
        domain = domain[4:]

    return domain


def is_same_domain(first_url: str, second_url: str) -> bool:
    """
    Return True if both URLs belong to the same domain.
    """

    first_domain = get_normalized_domain(first_url)
    second_domain = get_normalized_domain(second_url)

    return first_domain == second_domain


def find_link_container(
    soup: BeautifulSoup,
    css_selector: str | None,
    container_text: str | None,
) -> Tag:
    """
    Find the HTML container from which links should be extracted.

    Priority:
    1. A supplied CSS selector.
    2. A table or navigation container containing the supplied text.
    3. The entire page.
    """

    if css_selector:
        container = soup.select_one(css_selector)

        if container is None:
            raise RuntimeError(f"No element matched CSS selector: {css_selector}")

        return container

    if container_text:
        target = container_text.casefold()
        matching_containers: list[Tag] = []

        for container in soup.select(".collapsible.infobox, .navbox, table"):
            text = container.get_text(" ", strip=True).casefold()
            links = container.select("a[href]")

            if target in text and links:
                matching_containers.append(container)

        if not matching_containers:
            raise RuntimeError(
                "No suitable link container contained the text " f'"{container_text}".'
            )

        # Parent and child tables may both contain the requested text.
        # Prefer the matching container with the largest number of links.
        return max(
            matching_containers,
            key=lambda container: len(container.select("a[href]")),
        )

    return soup


def get_linked_urls(
    start_url: str,
    css_selector: str | None = None,
    container_text: str | None = None,
    url_contains: str | None = None,
    same_domain_only: bool = True,
    timeout: float = 20,
) -> list[str]:
    """
    Download a starting page and return matching linked URLs.

    The result is deduplicated and sorted alphabetically.
    """

    if url_contains is not None:
        url_contains = url_contains.strip()

        if not url_contains:
            url_contains = None

    response = requests.get(
        start_url,
        headers=HEADERS,
        timeout=timeout,
    )
    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser",
    )

    container = find_link_container(
        soup=soup,
        css_selector=css_selector,
        container_text=container_text,
    )

    urls: set[str] = set()

    for link in container.select("a[href]"):
        href = link.get("href")

        if not href:
            continue

        full_url = urljoin(
            start_url,
            href,
        )

        # Remove fragments such as #History.
        full_url, _fragment = urldefrag(full_url)

        parsed = urlparse(full_url)

        if parsed.scheme not in {"http", "https"}:
            continue

        if same_domain_only and not is_same_domain(
            start_url,
            full_url,
        ):
            continue

        if url_contains and url_contains not in full_url:
            continue

        urls.add(full_url)

    return sorted(urls)


if __name__ == "__main__":
    test_url = "https://dwarffortresswiki.org/index.php/Adder_man"

    test_urls = get_linked_urls(
        start_url=test_url,
        container_text="Creatures",
        url_contains="index.php",
    )

    print(f"Found {len(test_urls)} URLs")

    for test_link in test_urls[:20]:
        print(test_link)
