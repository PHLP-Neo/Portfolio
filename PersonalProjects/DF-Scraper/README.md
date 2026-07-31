# Dwarf Fortress Wiki Scraper

A reusable Python web scraper for extracting structured information from MediaWiki-based websites.

Originally developed for the **Dwarf Fortress Wiki**, the scraper can automatically discover linked pages from a starting page and extract specific information from each linked page, exporting the results as a CSV file.

Unlike a one-off scraper, this project separates **link discovery** from **content extraction**, making it easy to support additional extraction strategies in the future.

---

## Features

- Extract linked pages from a MediaWiki page
- Locate link containers using either:
  - CSS selectors
  - Container text
- Restrict scraping to the same domain
- Optional URL filtering
- Export results to CSV
- Immediate CSV flushing to avoid data loss during long runs
- Configurable request delay
- Multiple extraction modes

Current extraction modes include:

### Sentence Extraction

Searches each page for a sentence beginning with a specified prefix.

Example:

```
Some dwarves like aardvarks for their snout and their long ears.
```

### RAW Token Extraction

Extracts values from Dwarf Fortress RAW data embedded inside wiki pages.

Example:

```
[DESCRIPTION:A large adder with the torso and arms of a man.]
```

becomes

```
A large adder with the torso and arms of a man.
```

---

# Project Structure

```
DF-Scraper/
│
├── link_extractor.py
├── sentence_extractor.py
├── main.py
└── README.md
```

### `link_extractor.py`

Responsible for:

- downloading the starting page
- locating the desired HTML container
- collecting linked URLs
- filtering links
- removing duplicates

### `sentence_extractor.py`

Contains independent extraction strategies.

Current extractors:

- `extract_matching_sentence()`
- `extract_raw_token()`

New extractors can be added without modifying the rest of the project.

### `main.py`

Coordinates the workflow:

1. Parse command-line arguments
2. Discover linked pages
3. Select extraction mode
4. Process every page
5. Export results to CSV

---

# Requirements

- Python 3.11+
- requests
- beautifulsoup4

Install dependencies:

```bash
pip install requests beautifulsoup4
```

---

# Usage

## Sentence Extraction

Example:

```bash
python main.py sentence \
"https://dwarffortresswiki.org/index.php/Adder_man" \
"Some dwarves like" \
preferences.csv \
--container-text "Creatures"
```

Output:

| url | result |
|-----|--------|
| Aardvark | Some dwarves like aardvarks... |
| Adder | Some dwarves like adders... |

---

## RAW Extraction

Example:

```bash
python main.py raw \
"https://dwarffortresswiki.org/index.php/Adder_man" \
DESCRIPTION \
descriptions.csv \
--container-text "Creatures"
```

Output:

| url | result |
|-----|--------|
| Aardvark | A small burrowing mammal... |
| Adder | A small venomous snake... |

---

# Command Line Arguments

| Argument | Description |
|----------|-------------|
| mode | Extraction mode (`sentence` or `raw`) |
| start_url | Starting page |
| query | Sentence prefix or RAW token |
| output_file | CSV output |
| --selector | CSS selector for link container |
| --container-text | Find container by text |
| --url-contains | Restrict URLs containing text |
| --allow-external-links | Allow links from other domains |
| --delay | Delay between requests |
| --timeout | Request timeout |
| --limit | Limit number of pages (useful for testing) |

---

# Example Workflow

```
Starting Page
       │
       ▼
Locate Link Container
       │
       ▼
Extract URLs
       │
       ▼
Filter URLs
       │
       ▼
Download Each Page
       │
       ▼
Extract Information
       │
       ▼
Export CSV
```

---

# Design

The project follows a modular architecture.

```
             main.py
                 │
     ┌───────────┴───────────┐
     │                       │
link_extractor.py   sentence_extractor.py
                             │
          ┌──────────────────┴──────────────────┐
          │                                     │
extract_matching_sentence()      extract_raw_token()
```

This separation allows new extraction strategies to be added without changing the scraping pipeline.

---

# Skills Demonstrated

- Python
- Object-Oriented Design
- Web Scraping
- HTML Parsing (BeautifulSoup)
- HTTP Requests
- Command-Line Interface (argparse)
- Regular Expressions
- CSV Processing
- Modular Software Architecture
- Error Handling
- Data Extraction
- Clean Code Principles

---

# Future Improvements

Potential enhancements include:

- Parallel page downloads
- Retry and backoff strategy
- Resume interrupted scraping sessions
- JSON export
- YAML configuration files
- Progress bars (`tqdm`)
- Plugin-based extraction system
- Support for additional MediaWiki websites
- Additional extraction modes
- Automatic namespace filtering
- Logging system

---

# License

This project is intended for educational and research purposes.

Please respect the target website's Terms of Service and avoid excessive request rates when scraping public websites.