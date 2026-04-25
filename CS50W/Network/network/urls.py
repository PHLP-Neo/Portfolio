
from django.urls import path

from . import views

urlpatterns = [
    ## v this is all posts v
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following, name="following"),
    ## v this is new post v
    path("new_post", views.new_post, name="new_post"),
    path("toggle_follow/<str:user_id>", views.toggle_follow, name="toggle_follow"),
    path("toggle_like/<int:post_id>/", views.toggle_like, name="toggle_like"),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    ## v this is profile page v
    path("user/<str:user_id>",views.userstats, name="userstats"),
]
