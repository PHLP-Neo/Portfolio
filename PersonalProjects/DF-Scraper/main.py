from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path
from typing import TextIO

from link_extractor import get_linked_urls
from sentence_extractor import (
    extract_matching_sentence,
    extract_raw_token,
)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Extract links from a starting page, inspect each "
            "linked page, and save the extracted results to CSV."
        )
    )

    parser.add_argument(
        "mode",
        choices=[
            "sentence",
            "raw",
        ],
        help=(
            "'sentence' searches for prose beginning with a "
            "specified prefix. 'raw' extracts the value of a "
            "bracketed RAW token such as DESCRIPTION."
        ),
    )

    parser.add_argument(
        "start_url",
        help=("Starting page containing the links that should " "be inspected."),
    )

    parser.add_argument(
        "query",
        help=("Sentence prefix in sentence mode, or RAW token " "name in raw mode."),
    )

    parser.add_argument(
        "output_file",
        help="Name or path of the output CSV file.",
    )

    parser.add_argument(
        "--selector",
        default=None,
        help=(
            "Optional CSS selector identifying the container "
            "from which links should be extracted."
        ),
    )

    parser.add_argument(
        "--container-text",
        default=None,
        help=(
            "Optional text used to locate the container from "
            "which links should be extracted."
        ),
    )

    parser.add_argument(
        "--url-contains",
        default=None,
        help=(
            "Only process URLs containing this text. In Git "
            "Bash, use 'index.php' rather than '/index.php/' "
            "to avoid automatic path conversion."
        ),
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=1.5,
        help=("Delay in seconds between page requests. " "Default: 1.5"),
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=20,
        help=(
            "Request timeout in seconds while downloading the "
            "starting page. Default: 20"
        ),
    )

    parser.add_argument(
        "--allow-external-links",
        action="store_true",
        help="Allow links pointing to external domains.",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help=("Maximum number of linked pages to process. " "Useful during testing."),
    )

    return parser.parse_args()


def write_result(
    writer: csv.DictWriter,
    csv_file: TextIO,
    url: str,
    result: str | None,
    status: str,
    error: str,
) -> None:
    """
    Write one result to the CSV file and save it immediately.
    """

    writer.writerow(
        {
            "url": url,
            "result": result or "",
            "status": status,
            "error": error,
        }
    )

    csv_file.flush()


def extract_result(
    mode: str,
    url: str,
    query: str,
) -> str | None:
    """
    Select and run the requested extraction strategy.
    """

    if mode == "sentence":
        return extract_matching_sentence(
            url=url,
            prefix=query,
        )

    if mode == "raw":
        return extract_raw_token(
            url=url,
            token_name=query,
        )

    raise ValueError(f"Unsupported extraction mode: {mode}")


def main() -> None:
    args = parse_arguments()

    if args.limit is not None and args.limit < 1:
        raise ValueError("--limit must be at least 1.")

    output_path = Path(args.output_file)

    urls = get_linked_urls(
        start_url=args.start_url,
        css_selector=args.selector,
        container_text=args.container_text,
        url_contains=args.url_contains,
        same_domain_only=not args.allow_external_links,
        timeout=args.timeout,
    )

    if args.limit is not None:
        urls = urls[: args.limit]

    if not urls:
        raise RuntimeError("No matching URLs were found on the starting page.")

    print(f"Found {len(urls)} candidate URLs.")

    with output_path.open(
        "w",
        newline="",
        encoding="utf-8-sig",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "url",
                "result",
                "status",
                "error",
            ],
        )

        writer.writeheader()

        for index, url in enumerate(
            urls,
            start=1,
        ):
            try:
                result = extract_result(
                    mode=args.mode,
                    url=url,
                    query=args.query,
                )

                if result is None:
                    status = "not_found"
                else:
                    status = "success"

                error = ""

            except Exception as exception:
                result = None
                status = "error"
                error = str(exception)

            write_result(
                writer=writer,
                csv_file=csv_file,
                url=url,
                result=result,
                status=status,
                error=error,
            )

            print(f"[{index}/{len(urls)}] " f"{status}: {url}")

            if index < len(urls):
                time.sleep(max(args.delay, 0))

    print(f"Results written to: {output_path}")


if __name__ == "__main__":
    main()
