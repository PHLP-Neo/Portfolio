# Capstone Gallery

## Overview

Capstone Gallery is a web application inspired by image gallery and image board websites such as Danbooru. The application allows registered users to upload images, organize them using descriptive tags, browse uploaded content, search images by title, browse images by tag, leave comments, like images asynchronously, and delete images that they own. Visitors who are not logged in can still browse the gallery and view image details, while authenticated users gain access to all interactive features.

The primary objective of this project was to combine the major concepts introduced throughout CS50's Web Programming with Python and JavaScript into a single cohesive application. Rather than concentrating on one aspect of Django, the project integrates authentication, relational database modelling, media uploads, template inheritance, JavaScript, AJAX, responsive design, pagination, and file management.

Although the application is intentionally smaller than a production image hosting website, it demonstrates the complete lifecycle of user-generated content. A user can upload an image, describe it using tags, browse and search existing content, interact with other users through comments and likes, and remove previously uploaded images when they are no longer wanted.

---

# Distinctiveness and Complexity

This project satisfies the capstone requirements because it is designed as a complete image management application rather than an extension of any previous CS50W project. While the course projects each focus on a particular topic, this application combines many different concepts into a single workflow centred around media management.

The defining characteristic of the application is that uploaded images are treated as the primary resource. Every major feature revolves around an image and its associated metadata. Users are able to upload images together with a title and description, assign descriptive tags, browse images through pagination, locate images using either text search or tag navigation, interact with other users through comments and likes, and finally delete images together with their uploaded files. The project therefore focuses on managing the complete lifecycle of uploaded media instead of textual documents or social posts.

One of the most significant design decisions was the database structure. Instead of storing every piece of information inside a single table, the application separates images, tags, comments and users into independent models connected through relational fields. Tags are implemented using a many-to-many relationship. This allows a single image to contain multiple tags while also allowing every tag to reference many different images. During image upload, the application parses the user supplied tag string into individual tags, creating new database records only when necessary before establishing the many-to-many relationships. This design avoids duplicated tag records and makes browsing by tag efficient.

User interaction also required several different relationship types. Comments are implemented as a one-to-many relationship because every comment belongs to exactly one image while each image may contain many comments. Likes are implemented using another many-to-many relationship between users and images. This allows each user to like many images while every image can be liked by many users. Choosing the appropriate relationship for each feature required careful database modelling rather than storing all information in simple text fields.

Unlike ordinary HTML forms, image uploading requires binary file handling. The application therefore uses Django's `ImageField`, multipart form submission, and `request.FILES` to process uploaded images. Uploaded files are stored inside the project's media directory while the database stores only references to those files. When an image is deleted by its owner, both the database record and the uploaded file are removed, preventing orphaned files from remaining on disk. This required coordinating Django's model layer with its file storage system.

Another feature demonstrating increased complexity is the implementation of asynchronous likes. Rather than refreshing the entire page whenever a user clicks the Like button, JavaScript sends an asynchronous POST request using the Fetch API. Django processes the request, updates the database, and returns a `JsonResponse` containing the updated like information. JavaScript then modifies only the relevant portion of the page without requiring a complete reload. This combines Django views, JavaScript, JSON communication, and DOM manipulation into a single feature.

The gallery interface also introduces additional functionality beyond simply displaying uploaded images. Pagination prevents large numbers of images from being loaded onto a single page while search allows users to locate images by title using Django ORM queries. Tag pages provide an alternative navigation method by displaying all images associated with a selected tag. Together these features demonstrate different methods of querying and presenting relational data.

Finally, the project attempts to provide a responsive user interface. Bootstrap's responsive grid system is used so that the gallery adapts to different screen sizes, while custom CSS ensures uploaded images remain visually consistent. Although the visual design remains intentionally simple, the application is usable on both desktop and mobile devices.

While none of these individual features would be especially large in isolation, integrating them into a coherent application required coordinating many independent components of Django. Uploading an image involves authentication, form validation, file handling, media storage, database insertion, tag parsing, relationship creation, and template rendering. Viewing an image combines relational queries, conditional template rendering, comments, likes, and deletion permissions. Asynchronous liking introduces an entirely different communication path between browser and server. Collectively, the project demonstrates most of the major topics introduced throughout the course in a single application.

---

# Project Structure

## manage.py

This is Django's standard management script and is used for running the development server, applying database migrations, creating administrative users, and executing other management commands.

## requirements.txt

Lists all Python packages required to run the application, including Django and Pillow for image handling.

---

## capstone/

### settings.py

Contains the project's configuration. This includes installed applications, database configuration, media and static file settings, authentication configuration, and development settings.

### urls.py

Defines the project's top-level URL configuration and configures Django to serve uploaded media files while running the development server.

---

## gallery/

### models.py

Defines the application's database models including `ImagePost`, `Tag`, and `Comment`. The file also defines the many-to-many relationships used for tags and likes together with the one-to-many relationship used for comments.

### views.py

Contains the application's primary logic. This file implements gallery browsing, pagination, searching, tag browsing, image upload, comment creation, asynchronous liking through `JsonResponse`, image deletion, user registration, login, and logout.

### urls.py

Maps URL patterns to the corresponding view functions.

### forms.py

Defines the `ImagePostForm` used to validate uploaded image information before saving it into the database.

### admin.py

Registers application models with Django's administration interface.

### tests.py

Contains automated tests for selected application components.

---

## templates/gallery/

### layout.html

Provides the shared layout used by every page including the navigation bar, Bootstrap stylesheet, and template blocks.

### index.html

Displays the paginated gallery and search form.

### upload.html

Displays the image upload form.

### detail.html

Displays an individual image together with its description, tags, comments, like button, and delete option.

### search.html

Displays search results.

### tag.html

Displays all images associated with a selected tag.

### login.html

Provides the user login page.

### register.html

Provides the user registration page.

---

## static/gallery/

### styles.css

Contains custom CSS used to style the gallery, responsive image layout, and general page appearance.

---

## media/

Stores uploaded image files while the application is running locally.

---

# How to Run

1. Clone the repository.

2. Create and activate a Python virtual environment.

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Apply database migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create an administrator account if desired.

```bash
python manage.py createsuperuser
```

6. Start the development server.

```bash
python manage.py runserver
```

7. Open a browser and navigate to:

```
http://127.0.0.1:8000/
```

Uploaded images are stored inside the `media/` directory during development.

---

# Additional Information

This application was intentionally designed to remain within the technologies covered by CS50W. No external REST framework, cloud storage service, third-party authentication provider, or frontend framework was used. Instead, the project relies on Django's built-in authentication system, ORM, template engine, ModelForms, and media handling together with JavaScript's Fetch API and Bootstrap.

Several features commonly found in production image hosting websites were intentionally omitted in order to keep the project focused on the concepts taught during the course. Examples include image moderation, automatic thumbnail generation, recommendation systems, cloud storage, user roles, and image metadata extraction. The goal of the project was not to recreate a commercial image hosting platform, but to demonstrate a comprehensive understanding of the material presented throughout CS50's Web Programming with Python and JavaScript.

Overall, Capstone Gallery demonstrates authentication, relational database design, media uploads, template inheritance, pagination, responsive web design, asynchronous JavaScript communication, and server-side rendering within a single Django application.