from django.urls import path
from . import views

urlpatterns = [
    path("", views.gallery, name="gallery"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("upload/", views.upload_post, name="upload_post"),
]