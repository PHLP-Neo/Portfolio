import csv
import time

from inspect_page import get_creature_urls
from my_scraper import extract_matching_sentence

START_URL = "https://dwarffortresswiki.org/index.php/Adder_man"
PREFIX = "Some dwarves like"
REQUEST_DELAY = 1.5
OUTPUT_FILE = "PersonalProjects\DF-Scraper\dwarf_creature_preferences.csv"


def main() -> None:
    creature_urls = get_creature_urls(START_URL)

    print(f"Found {len(creature_urls)} candidate URLs.")

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8-sig",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "url",
                "sentence",
                "status",
                "error",
            ],
        )

        writer.writeheader()

        for index, url in enumerate(creature_urls[:20], start=1):
            sentence = None
            status = "success"
            error_message = ""

            try:
                sentence = extract_matching_sentence(
                    url,
                    PREFIX,
                )

                if sentence is None:
                    status = "not_found"

            except Exception as error:
                status = "error"
                error_message = str(error)

            writer.writerow(
                {
                    "url": url,
                    "sentence": sentence or "",
                    "status": status,
                    "error": error_message,
                }
            )

            # Ensure each result is saved immediately.
            csv_file.flush()

            print(f"[{index}/{len(creature_urls)}] " f"{status}: {url}")

            time.sleep(REQUEST_DELAY)

    print(f"\nResults written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
