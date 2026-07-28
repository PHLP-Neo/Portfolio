import time

from inspect_page import get_creature_urls
from my_scraper import extract_matching_sentence

START_URL = "https://dwarffortresswiki.org/index.php/Adder_man"
PREFIX = "Some dwarves like"
REQUEST_DELAY = 1.5


def main() -> None:
    creature_urls = get_creature_urls(START_URL)

    print(f"Found {len(creature_urls)} candidate URLs.\n")

    for url in creature_urls[:10]:
        try:
            sentence = extract_matching_sentence(
                url,
                PREFIX,
            )

            print("URL:", url)
            print("Sentence:", sentence)
            print()

        except Exception as error:
            print("URL:", url)
            print("Error:", error)
            print()

        time.sleep(REQUEST_DELAY)


if __name__ == "__main__":
    main()
