# CS50 Web - Wiki Encyclopedia

![Screenshot or demo GIF](screenshot.png)

**Full-stack Wikipedia clone** built with Django: Markdown-powered entries, search/edit/random pages, HTML rendering.

## Features Implemented
- **Entry Pages**: `wiki/TITLE` shows converted Markdown (headings, bold, lists, links) or 404.
- **Index/Search**: List all entries; substring search redirects or shows results.
- **CRUD**: New/edit pages with title/content forms (error on duplicates).
- **Random**: Sidebar link to random entry.
- Tech: Django views/forms, `markdown2` lib, file-based storage (`entries/`).[file:77]

**What I Learned**: Regex for custom Markdown parsing, form validation, dynamic routing.
