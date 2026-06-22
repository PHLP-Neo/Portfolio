# Capstone Booru

## Overview

Capstone Booru is a tag-based image sharing and archive platform inspired by websites such as Danbooru. Users can register accounts, upload images, organize content using tags, browse images through tag-based navigation, leave comments, and save favorite posts.

The project was developed using Django and JavaScript as the final project for CS50's Web Programming with Python and JavaScript.

The primary goal of the project is to create a searchable image archive where content discovery is driven by tags rather than chronological feeds. Unlike a traditional social network, users primarily interact with images through tagging, searching, favoriting, and commenting.

\---

## Distinctiveness and Complexity

This project is distinct from the projects completed throughout CS50W.

Unlike Project 4 (Social Network), this application is not centered around user posts, following relationships, or activity feeds. Instead, it focuses on image management, tag organization, and content discovery through search and categorization.

Unlike Project 2 (Commerce), this application does not involve auctions, bidding, listings, or financial transactions. Instead, it implements a custom media management workflow with image uploads, tagging systems, comments, favorites, user profiles, and image lifecycle management.

The application combines several interconnected features:

* User authentication and registration
* Image upload and storage
* Many-to-many tag relationships
* Multi-tag search functionality
* User profiles
* Comment system
* Favorite system using JavaScript Fetch API
* Responsive mobile-friendly interface
* Media file cleanup during image replacement and deletion

The project uses multiple Django models with relationships between users, posts, tags, comments, and favorites. JavaScript is used for asynchronous favorite functionality and image previews.

\---

## Features

### User Accounts

Users can:

* Register new accounts
* Log in and log out
* Access personal profile pages

Passwords are managed using Django's built-in authentication framework and are stored as secure hashes rather than plaintext.

### Image Upload

Authenticated users can:

* Upload images
* Add titles and descriptions
* Assign multiple tags

Uploaded images are stored using Django's ImageField and served through Django's media system.

### Tag System

Images can be assigned multiple tags.

Users can:

* Browse tag pages
* Search using one or more tags
* Discover related content through tag navigation

The search system supports multi-tag filtering where all specified tags must be present.

### Favorites

Users can favorite and unfavorite images.

This functionality is implemented using JavaScript and the Fetch API. Favorites update asynchronously without requiring a full page refresh.

### Comments

Authenticated users can leave comments on image posts.

Comments are associated with both the user and the image being commented on.

### Profiles

Each user has a profile page displaying:

* Uploaded images
* Favorited images

### Permissions

Only the uploader of an image may:

* Edit the image
* Delete the image

Unauthorized users receive a forbidden response.

### Media Cleanup

When an image is replaced, the previous file is automatically removed from disk.

When an image post is deleted, the associated image file is also deleted from the media directory. This prevents orphaned files from accumulating on the server.

### Responsive Design

The interface adapts to smaller screen sizes using CSS media queries. The gallery layout, navigation bar, and forms remain usable on mobile devices.

\---

## Database Models

### Image Post

Stores:

* Title
* Description
* Uploaded image
* Upload timestamp
* Uploader

### Tag

Stores tag names used for categorizing images.

Images and tags are connected through a many-to-many relationship.

### Comment

Stores:

* Author
* Image post
* Comment content
* Creation timestamp

### Favorite

Stores user favorites and links users to image posts they have saved.

\---

## Design Decisions

### Tag-Based Navigation

A tag-based system was chosen because it is the defining characteristic of booru-style websites. A single image can belong to many tags simultaneously, making a many-to-many relationship more flexible than a category-based structure.

### AJAX Favorites

Favorites are implemented using JavaScript Fetch requests instead of traditional form submissions. This allows the page to update instantly without a reload and demonstrates front-end and back-end interaction.

### Media File Management

By default, Django does not automatically remove uploaded files when database records are deleted. Custom cleanup logic was implemented to remove old images during replacement and deletion, preventing wasted disk space and orphaned files.

### User Profiles

Profiles provide a simple way for users to revisit both their own uploads and their favorite content, improving usability without introducing the complexity of a social network.

\---

## JavaScript Functionality

JavaScript is used in two primary areas.

### Favorite System

The favorite button communicates with a Django endpoint using the Fetch API. The page updates dynamically without reloading when a user favorites or unfavorites an image.

### Image Preview

Users can preview selected images before submitting an upload form. The preview updates instantly when a new file is selected.

\---

## File Structure

* `capstone/` – Django project configuration
* `booru/` – Main application
* `templates/` – HTML templates
* `static/` – CSS and frontend assets
* `media/` – Uploaded images
* `requirements.txt` – Project dependencies

\---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

\---

## Future Improvements

Potential future enhancements include:

* Image voting system
* Tag aliases
* Image moderation workflow
* Pagination
* Infinite scrolling
* Advanced search operators
* User avatars
* Image collections
* Public API

