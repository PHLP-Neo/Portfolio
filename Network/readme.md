# CS50 Web - Network Social Platform

![Screenshot or demo GIF](screenshot.png)

**Twitter-like social network** with Django/JS: posts/follow/likes/pagination/edit.

## Features Implemented
- **Posts**: New post form → All Posts/Following (reverse chrono, 10/page, prev/next).
- **Profiles**: User posts/followers count, follow/unfollow toggle (no self-follow).
- **Interactions**: Edit own posts (JS textarea/save, no reload), like/unlike (async fetch, update count).
- Tech: Django auth/models (Post/UserFollows/Likes), JS for real-time UI.[user spec]

**What I Learned**: Pagination queries, async like/edit without page reloads.
