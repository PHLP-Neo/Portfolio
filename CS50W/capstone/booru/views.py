from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ImagePostForm
from .models import ImagePost, Tag

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

@login_required
def upload_post(request):
    if request.method == "POST":
        form = ImagePostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.uploader = request.user
            post.save()

            tag_string = form.cleaned_data["tag_string"]
            tag_names = tag_string.split()

            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name.lower())
                post.tags.add(tag)

            return redirect("post_detail", post_id=post.id)

    else:
        form = ImagePostForm()

    return render(request, "booru/upload.html", {
        "form": form
    })

def tag_detail(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name.lower())
    posts = tag.posts.all().order_by("-created_at")

    return render(request, "booru/gallery.html", {
        "posts": posts,
        "page_title": f"Tag: {tag.name}"
    })


def search_posts(request):
    query = request.GET.get("q", "").strip().lower()
    posts = ImagePost.objects.all().order_by("-created_at")

    if query:
        tag_names = query.split()

        for tag_name in tag_names:
            posts = posts.filter(tags__name=tag_name)

        posts = posts.distinct()

    return render(request, "booru/gallery.html", {
        "posts": posts,
        "query": query,
        "page_title": "Search results"
    })