from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, JsonResponse
from django.views.decorators.http import require_POST


from .forms import ImagePostForm
from .models import ImagePost, Tag, Favorite

# Create your views here.


def gallery(request):
    posts = ImagePost.objects.all().order_by("-created_at")
    return render(request, "booru/gallery.html", {
        "posts": posts
    })


def post_detail(request, post_id):
    post = get_object_or_404(ImagePost, id=post_id)

    is_favorited = False

    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(
            user=request.user,
            post=post
        ).exists()

    return render(request, "booru/post_detail.html", {
        "post": post,
        "is_favorited": is_favorited
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

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(ImagePost, id=post_id)

    if post.uploader != request.user:
        return HttpResponseForbidden("You cannot edit this post.")

    if request.method == "POST":
        form = ImagePostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save()

            post.tags.clear()
            tag_string = form.cleaned_data["tag_string"]
            tag_names = set(tag_string.split())

            for tag_name in tag_names:
                tag_name = tag_name.lower().strip()

                if tag_name:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)

            return redirect("post_detail", post_id=post.id)

    else:
        existing_tags = " ".join(tag.name for tag in post.tags.all())
        form = ImagePostForm(instance=post, initial={
            "tag_string": existing_tags
        })

    return render(request, "booru/edit_post.html", {
        "form": form,
        "post": post
    })


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(ImagePost, id=post_id)

    if post.uploader != request.user:
        return HttpResponseForbidden("You cannot delete this post.")

    if request.method == "POST":
        post.delete()
        return redirect("gallery")

    return render(request, "booru/delete_post.html", {
        "post": post
    })

@login_required
@require_POST
def toggle_favorite(request, post_id):
    post = get_object_or_404(ImagePost, id=post_id)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        favorite.delete()
        favorited = False
    else:
        favorited = True

    return JsonResponse({
        "favorited": favorited,
        "count": post.favorites.count()
    })