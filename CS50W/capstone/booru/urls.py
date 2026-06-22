from django.urls import path
from . import views

urlpatterns = [
    path("", views.gallery, name="gallery"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("upload/", views.upload_post, name="upload_post"),
    path("tag/<str:tag_name>/", views.tag_detail, name="tag_detail"),
    path("search/", views.search_posts, name="search_posts"),
    path("post/<int:post_id>/edit/", views.edit_post, name="edit_post"),
    path("post/<int:post_id>/delete/", views.delete_post, name="delete_post"),
]