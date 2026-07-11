# Capstone Gallery

## Overview

Capstone Gallery is a Django web application inspired by image gallery
websites such as Danbooru. Users can register, log in, upload images,
assign tags, browse the gallery, search by title, browse by tag, comment
on images, like or unlike images asynchronously, and delete images that
they own.

The project was developed using the technologies covered throughout
CS50's Web Programming with Python and JavaScript. It combines Django
models, authentication, templates, forms, JavaScript, AJAX, file
uploads, pagination, and responsive design into a single application.

## Distinctiveness and Complexity

This project satisfies the CS50W capstone requirements because it is not
a modification of any of the course projects. While it borrows ideas
from image board websites, it was designed and implemented as a
standalone application.

Unlike the Wiki project, this application manages uploaded image files
instead of Markdown pages. Unlike Commerce, it focuses on media
management rather than auctions. Unlike Network, it introduces media
uploads, tagging, and gallery browsing. Unlike Mail, it combines
traditional server-rendered pages with AJAX interactions.

The project integrates many concepts taught throughout the course:

-   Django authentication
-   Django models and ORM relationships
-   ModelForms
-   Image uploads using ImageField
-   Local media storage
-   Many-to-many relationships for tags and likes
-   One-to-many relationships for comments
-   Pagination using Django's Paginator
-   Search using Django ORM queries
-   AJAX like/unlike functionality using JavaScript `fetch()` and
    `JsonResponse`
-   Responsive layout using Bootstrap and CSS
-   Secure deletion of uploaded image files together with their database
    records

Although each individual feature is relatively straightforward,
integrating them into a coherent web application required coordinating
models, views, templates, forms, JavaScript, CSS, media configuration,
and URL routing.

## Project Structure

### manage.py

Entry point for Django management commands.

### requirements.txt

Lists all required Python packages.

### capstone/

-   **settings.py** -- Django project configuration, installed apps,
    media configuration, authentication model, and static file settings.
-   **urls.py** -- Project URL routing and development media
    configuration.

### gallery/

-   **models.py** -- Defines the User, ImagePost, Tag, and Comment
    models together with their relationships.
-   **views.py** -- Implements gallery browsing, searching, tag
    browsing, image upload, comments, likes, authentication, pagination,
    and deletion.
-   **urls.py** -- Maps URL patterns to view functions.
-   **forms.py** -- Defines the image upload form.
-   **admin.py** -- Registers models with the Django admin site.
-   **tests.py** -- Contains basic automated tests.

### templates/gallery/

-   **layout.html** -- Shared page layout.
-   **index.html** -- Main gallery page.
-   **detail.html** -- Individual image page.
-   **upload.html** -- Image upload page.
-   **search.html** -- Search results.
-   **tag.html** -- Images associated with a tag.
-   **login.html** -- Login page.
-   **register.html** -- Registration page.

### static/gallery/

Contains the project's custom CSS.

### media/

Stores uploaded image files during development.

## How to Run

1.  Clone the repository.
2.  Create and activate a Python virtual environment.
3.  Install dependencies:

``` bash
pip install -r requirements.txt
```

4.  Apply migrations:

``` bash
python manage.py makemigrations
python manage.py migrate
```

5.  Create an administrator account:

``` bash
python manage.py createsuperuser
```

6.  Start the server:

``` bash
python manage.py runserver
```

7.  Open your browser at:

``` text
http://127.0.0.1:8000/
```

## Additional Information

Uploaded images are stored locally inside the `media/` directory during
development. Users may delete images that they own; the application
deletes both the uploaded file and the associated database record.

The application intentionally focuses on core functionality rather than
advanced features such as cloud storage, AI image tagging, moderation
workflows, recommendation systems, or thumbnail generation. The goal was
to build a complete Django application demonstrating the concepts
covered throughout CS50W while keeping the implementation maintainable
and understandable.
