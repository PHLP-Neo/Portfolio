from django.shortcuts import render, get_object_or_404
from .models import ImagePost

# Create your views here.


def gallery(request):
    posts = ImagePost.objects.all().order_by("-created_at")
    return render(request, "booru/gallery.html", {
        "posts": posts
    })


def post_detail(request, post_id):
    post = get_object_or_404(ImagePost, id=post_id)
    return render(request, "booru/post_detail.html", {
        "post": post
    })