# Capstone Booru

## Overview

Capstone Booru is a tag-based image sharing and archive platform inspired by booru-style websites such as Danbooru. The application allows users to register accounts, upload images, organize content using tags, browse content through tag-based navigation, comment on images, and maintain personal collections of favorite posts.

The project was developed as the final project for CS50's Web Programming with Python and JavaScript using Django as the backend framework and JavaScript for client-side interactivity.

Unlike a traditional social network that focuses on chronological feeds and user relationships, Capstone Booru focuses on content discovery. Images are organized through a flexible tagging system, allowing users to search for content using one or more tags and navigate through related images.

The project demonstrates full-stack web development concepts including database design, authentication, authorization, file uploads, asynchronous JavaScript communication, responsive design, and media management.

---

## Distinctiveness and Complexity

This project is substantially different from the projects completed during CS50W.

Unlike Project 4 (Social Network), this application is not centered around user posts, likes, following relationships, or activity feeds. Instead, it focuses on image management, tag organization, and content discovery through searching and categorization.

Unlike Project 2 (Commerce), this application does not involve auctions, listings, bids, or transactions. Instead, it implements a custom workflow for media storage, image management, tagging, comments, favorites, and profile organization.

Several features interact closely throughout the application:

- User authentication and registration
- Image upload and storage
- Many-to-many tag relationships
- Multi-tag search
- User profiles
- Comment system
- Favorite system using JavaScript Fetch API
- Responsive mobile-friendly interface
- Automatic media cleanup
- Permission-controlled editing and deletion

The application contains multiple interconnected database models. Images can have many tags, users can comment on many images, and users can maintain personal collections of favorites. The search functionality dynamically filters images based on combinations of tags. The project also manages uploaded media files on disk and includes custom cleanup logic to prevent orphaned files from accumulating.

These features require coordination between Django models, forms, views, templates, JavaScript, authentication systems, and filesystem operations, making the project significantly more complex than a basic CRUD application.

---

## Core Features

### User Accounts

Users can:

- Register new accounts
- Log in and log out
- Access profile pages
- View their uploads
- View their favorite images

Passwords are managed using Django's built-in authentication framework and are stored as secure password hashes rather than plaintext values.

### Image Upload

Authenticated users can upload image files and provide:

- Title
- Description
- Tags

Uploaded images are stored using Django's ImageField and served through Django's media system.

### Tag System

The tagging system is the central feature of the application.

Users can:

- Assign multiple tags to an image
- Browse dedicated tag pages
- Search using multiple tags simultaneously
- Discover related content through tag navigation

Tags are implemented using a many-to-many relationship between images and tags.

### Search

The search system supports multiple tags in a single query.

For example:

- cat
- landscape
- cat landscape

When multiple tags are entered, only images containing all specified tags are returned.

### Favorites

Users can favorite and unfavorite images.

The favorite system is implemented asynchronously using JavaScript and the Fetch API, allowing favorite counts and button states to update without reloading the page.

### Comments

Authenticated users can leave comments on image posts.

Comments are linked to both the image and the user who created them.

### Profiles

Every user has a profile page displaying:

- Uploaded images
- Favorited images

This allows users to revisit both their own content and content they have saved.

### Permissions

Only the uploader of an image may:

- Edit the image
- Replace the image file
- Delete the image

Attempts to modify another user's content are rejected.

### Responsive Design

The interface adapts to different screen sizes using CSS media queries.

The navigation bar, gallery layout, forms, and image views remain usable on both desktop and mobile devices.

---

## System Architecture

### Upload Workflow

1. User submits the upload form.
2. Django validates the submitted data.
3. The image is saved to the media directory.
4. An ImagePost record is created.
5. Tags are created if they do not already exist.
6. Tag relationships are established.
7. User is redirected to the post detail page.

### Favorite Workflow

1. User clicks the favorite button.
2. JavaScript sends a Fetch API request.
3. Django toggles the favorite state.
4. Django returns a JSON response.
5. JavaScript updates the button and count without reloading the page.

### Comment Workflow

1. User submits a comment.
2. Django validates the form.
3. Comment is linked to both the user and image.
4. Comment is stored in the database.
5. User is redirected back to the image page.

---

## Database Design

### User

Django's built-in User model is used for authentication and account management.

### ImagePost

Stores:

- Title
- Description
- Image file
- Upload timestamp
- Uploader

Relationship:

- One user can upload many images.

### Tag

Stores tag names used to categorize images.

Relationship:

- One tag can belong to many images.
- One image can contain many tags.

### Comment

Stores:

- Author
- Image post
- Comment content
- Creation timestamp

Relationship:

- One image can contain many comments.
- One user can create many comments.

### Favorite

Stores favorite relationships between users and images.

Relationship:

- One user can favorite many images.
- One image can be favorited by many users.

---

## Design Decisions

### Why Use Tags Instead of Categories?

A booru-style website is fundamentally built around tags. Categories force an image into a single classification, while tags allow images to be associated with multiple concepts simultaneously.

For example, a single image may be tagged as:

- cat
- landscape
- sunset

This makes searching and discovery significantly more flexible.

### Why Use a Many-to-Many Relationship?

Tags naturally form a many-to-many relationship.

A single image may contain many tags, while a single tag may appear on many images. Using Django's many-to-many relationship simplifies querying and reflects the real-world structure of tagged content.

### Why Use AJAX Favorites?

The favorite system was intentionally implemented using JavaScript Fetch requests rather than traditional page reloads.

This provides:

- Better user experience
- Faster interactions
- Demonstration of asynchronous client-server communication

### Why Implement Media Cleanup?

During testing it became clear that deleting database records did not automatically remove uploaded files from disk.

Additional cleanup logic was implemented to:

- Remove files when posts are deleted
- Remove old files when images are replaced

This prevents orphaned files from consuming storage space.

---

## JavaScript Functionality

JavaScript is used in two major features.

### Favorite System

The favorite button communicates with a Django endpoint using the Fetch API.

The server returns JSON data which is processed by JavaScript to update the interface dynamically.

This demonstrates asynchronous communication between frontend and backend components.

### Image Preview

When users select an image during upload, JavaScript generates an immediate preview before submission.

This improves usability and provides instant visual feedback.

---

## Security Considerations

Several security mechanisms are implemented:

- Passwords are hashed by Django's authentication framework.
- CSRF protection is enabled for forms and authenticated actions.
- Uploading requires authentication.
- Commenting requires authentication.
- Favoriting requires authentication.
- Editing requires ownership of the post.
- Deletion requires ownership of the post.
- Unauthorized modification attempts return forbidden responses.

These protections help prevent unauthorized access and modification of content.

---

## Development Challenges

### Media File Management

One challenge encountered during development involved uploaded files.

Deleting a database record removes the image entry but does not automatically remove the associated file from disk. Additional logic was implemented to ensure uploaded files are properly cleaned up when images are replaced or deleted.

### Tag Editing

Maintaining tag consistency during image editing required rebuilding tag relationships whenever tags were updated. This ensured that search results remained accurate and synchronized with user changes.

### Responsive Layout

Early versions of the navigation bar did not display correctly on small screens. The layout was redesigned using CSS flexbox and responsive media queries to improve mobile usability.

---

## File Structure

- capstone/ – Django project configuration
- booru/ – Main application
- templates/ – HTML templates
- static/ – CSS and frontend assets
- media/ – Uploaded images
- requirements.txt – Project dependencies

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

The application will be available at:

http://127.0.0.1:8000/

---

## Future Improvements

Potential future enhancements include:

- Image voting system
- Tag aliases
- Image moderation workflow
- Pagination
- Infinite scrolling
- Advanced search operators
- User avatars
- Image collections
- Public API
- Image metadata extraction
- Bulk uploads

## Conclusion

Capstone Booru demonstrates the use of Django and JavaScript to build a complete web application centered around image management and discovery. The project combines authentication, media storage, many-to-many relationships, asynchronous JavaScript interactions, responsive design, and permission-based access control into a single cohesive application.
