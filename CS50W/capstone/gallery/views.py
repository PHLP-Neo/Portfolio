# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse

from .forms import ImagePostForm
from .models import User, ImagePost, Tag, Comment


def index(request):
    posts = ImagePost.objects.all().order_by("-timestamp")

    paginator = Paginator(posts, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    #from Network task
    return render(request, "gallery/index.html", {
        "page_obj": page_obj
    })

def search(request):
    if request.method == "POST":
        query = request.POST["q"]
        posts = ImagePost.objects.filter(title__icontains=query).order_by("-timestamp")

        return render(request, "gallery/search.html", {
            "query": query,
            "posts": posts
        })

    return HttpResponseRedirect(reverse("index"))


def tag(request, tag_name):
    try:
        tag = Tag.objects.get(name=tag_name)
    except Tag.DoesNotExist:
        return HttpResponse("Tag does not exist.")
    posts = tag.posts.all().order_by("-timestamp")
    return render(request, "gallery/tag.html", {
        "tag": tag,
        "posts": posts
    })

@login_required
def upload(request):
    if request.method == "POST":
        form = ImagePostForm(request.POST, request.FILES)
        # https://www.geeksforgeeks.org/python/python-uploading-images-in-django/
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            tag_text = request.POST["tag_text"]
            for raw_tag in tag_text.split():
                tag_name = raw_tag.lower()
                try:
                    tag = Tag.objects.get(name=tag_name)
                except Tag.DoesNotExist:
                    tag = Tag(name=tag_name)
                    tag.save()
                post.tags.add(tag)
            return HttpResponseRedirect(reverse("post_detail", kwargs={"post_id": post.id}))
        return render(request, "gallery/upload.html", {
            "form": form
        })
    return render(request, "gallery/upload.html", {
        "form": ImagePostForm()
    })

@login_required
def delete(request, post_id):
    try:
        post = ImagePost.objects.get(id=post_id)
    except ImagePost.DoesNotExist:
        return HttpResponse("Image post does not exist.")
    if request.user != post.owner:
        return HttpResponse("Permission denied.")
    if request.method == "POST":
        if post.image:
            post.image.delete(save=False)
        # from Rubber Duck and https://stackoverflow.com/questions/12888318/deleting-files-associated-with-model-django
        post.delete()
        return HttpResponseRedirect(reverse("index"))
    return HttpResponseRedirect(reverse("post_detail", kwargs={
        "post_id": post.id
    }))


def post_detail(request, post_id):
    try:
        post = ImagePost.objects.get(id=post_id)
    except ImagePost.DoesNotExist:
        return HttpResponse("Image post does not exist.")

    comments = Comment.objects.filter(post=post).order_by("-timestamp")

    return render(request, "gallery/detail.html", {
        "post": post,
        "comments": comments
    })


@login_required
def comment(request, post_id):
    if request.method == "POST":
        try:
            post = ImagePost.objects.get(id=post_id)
        except ImagePost.DoesNotExist:
            return HttpResponse("Image post does not exist.")
        body = request.POST["body"]
        if body != "":
            new_comment = Comment(post=post, owner=request.user, body=body)
            new_comment.save()
        return HttpResponseRedirect(reverse("post_detail", kwargs={"post_id": post.id}))
    return HttpResponseRedirect(reverse("index"))


@login_required
def like(request, post_id):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST request required."},
            status=400
        )
    try:
        post = ImagePost.objects.get(id=post_id)
    except ImagePost.DoesNotExist:
        return JsonResponse(
            {"error": "Image not found."},
            status=404
        )
    if request.user in post.liked_by.all():
        post.liked_by.remove(request.user)
        liked = False
    else:
        post.liked_by.add(request.user)
        liked = True
    return JsonResponse({
        "liked": liked,
        "likes": post.liked_by.count()
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "gallery/login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, "gallery/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "gallery/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "gallery/register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "gallery/register.html")
