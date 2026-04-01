from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import User,Post_listing
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json




def index(request):
    all_post = Post_listing.objects.all().order_by("-timestamp")
    p = Paginator(all_post, 10)
    page_no = request.GET.get("page")
    current_page = p.get_page(page_no)

    return render(request, "network/index.html",{
        "Posts":current_page
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def following(request):



    all_post = Post_listing.objects.filter(owner__in=request.user.following.all()).order_by("-timestamp")
    p = Paginator(all_post, 10)
    page_no = request.GET.get("page")
    current_page = p.get_page(page_no)

    return render(request, "network/following.html",{
        "Posts":current_page
    })

    return render(request, "network/following.html")

    pass

@login_required(login_url="/login?s=t")
def new_post(request):
    if request.method == "POST":
        title = request.POST["Title"]
        desc = request.POST["Desc"]
        time = datetime.now()
        owner = request.user
        likes = 0
        new_post = Post_listing(title=title, body = desc, timestamp = time, owner = owner, likes = 0)
        new_post.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/new_post.html")

@login_required(login_url="/login?s=t")
def userstats(request,user_id):

    user_post = Post_listing.objects.filter(owner=user_id).order_by("-timestamp")
    p = Paginator(user_post, 10)
    page_no = request.GET.get("page")
    current_page = p.get_page(page_no)
    target_user = User.objects.get(id=user_id)
    user_exist = False
    if request.user.following.filter(pk=target_user.id).exists():
        user_exist = True

    following_list = list(target_user.following.all())

    followed_by_list = list(target_user.followed_by.all())

    following_count = len(following_list)

    followed_by_count = len(followed_by_list)

    return render(request, "network/userstats.html",{
        "request_user":request.user,
        "viewing_user": target_user,
        "posts":current_page,
        "following":user_exist,
        "followings": following_list,
        "follow_count":following_count,
        "followed_count":followed_by_count
    })

@login_required(login_url="/login?s=t")
def toggle_follow(request,user_id):

    target_user = User.objects.get(id=user_id)
    
    if target_user in request.user.following.all():
        request.user.following.remove(target_user)
    else:
        request.user.following.add(target_user)
    
    return HttpResponseRedirect(reverse('userstats', kwargs={'user_id': user_id}))

@csrf_exempt
@login_required(login_url="/login?s=t")
def toggle_like(request,post_id):

    target_post = Post_listing.objects.get(id=post_id)
    user = request.user
    user_like_this_post = False

    if user in target_post.liked_person.all():
        target_post.liked_person.remove(user)
        target_post.likes -= 1
    else:
        target_post.liked_person.add(user)
        target_post.likes += 1
        user_like_this_post = True
    
    target_post.save()

    return JsonResponse({
        "user_like_this_post":user_like_this_post,
        "target_post_likes":target_post.likes
    })

# @login_required(login_url="/login?s=t")
# def following(request,user_id):
#     pass
@csrf_exempt
@login_required
def edit_post(request, post_id):
    post = Post_listing.objects.get(id=post_id)
    if request.user != post.owner:
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    
    if request.method == 'PUT':
        post.body = json.loads(request.body)['body']
        post.save()
        return JsonResponse({'body': post.body})
    
    return JsonResponse({'body': post.body})