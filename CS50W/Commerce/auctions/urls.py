from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name = "new_listing"),
    path("new_bids", views.new_bids, name = "new_bids"),
    path("new_comment", views.new_comment, name = "new_comment"),
    path("close_poll", views.close_poll, name = "close_poll"),
    path("add_to_fav", views.add_to_fav, name = "add_to_fav"),
    path("remove_from_fav", views.remove_from_fav, name = "remove_from_fav"),
    path("my_fav", views.my_fav, name = "my_fav"),
    path("category", views.category, name = "category"),
    path("listing/<str:listing_id>", views.show_listing, name = "show_listing"),
    path("category/<str:category_name>", views.deep_category, name = "deep_category"),
]

