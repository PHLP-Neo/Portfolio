from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload", views.upload, name="upload"),
    path("post/<int:post_id>", views.post_detail, name="post_detail"),
    path("post/<int:post_id>/comment", views.comment, name="comment"),
    path("post/<int:post_id>/like", views.like, name="like"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]