from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now
from .models import User, Auction_Listing, Bids, Bids, Comments
from django.db.models import Q

def index(request):
    return render(request, "auctions/index.html",{
        "listings":Auction_Listing.objects.all()
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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        message = ""
        try:
            code = request.GET.get('s', '')
            if code == "t":
                message = "This feature is for logged-in users only."
        except:
            pass
        finally:
            return render(request, "auctions/login.html",{
                "message":message
            })


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required(login_url="/login?s=t")
def new_listing(request):
    if request.method == "POST":
        name = request.POST["Name"]
        desc = request.POST["Desc"]
        category = request.POST["Category"]
        list_img = request.POST["Lis_Image"]
        Starting_bid = request.POST["Starting_Bid"]
        user = request.user
        new_listing = Auction_Listing(title=name, description = desc, listing_image_link = list_img, category = category, bid_price = Starting_bid, owner = user)
        new_listing.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/new_listing.html")

def show_listing(request, listing_id):
    try:
        listing = Auction_Listing.objects.get(id=listing_id)
    except:
        return HttpResponse(f"I dont know how you get here, but this entry ({listing_id}) does not exist")
    try:
        comments = Comments.objects.filter(comment_listing = listing)
        #print(comments)
    except:
        comments = False
        #print("comment gather failed")
    try:
        watchlist = User.objects.get(watchlist = listing)
        #print(comments)
    except:
        watchlist = False
    return render(request, "auctions/ind_listing.html", {
        "listing":listing,
        "comments":comments,
        "watchlist":watchlist
    })

@login_required(login_url="/login?s=t")
def new_bids(request):
    if request.method == "POST":
        listing_id = request.POST["bid_id"]
        listing = Auction_Listing.objects.get(id=listing_id)
        current_high_price = listing.bid_price
        price = int(request.POST["bid_price"])
        date = now()
        user = request.user
        if (price > current_high_price):
            new_bid = Bids(bid_owner = user, bid_listing = listing, bid_time = date, bid_price = price)
            listing.bid_price = price
            listing.save()
            new_bid.save()
            return HttpResponseRedirect(reverse("show_listing", kwargs={"listing_id":listing_id}))
        else:
            messages.error(request, "Higher Bids already exist, refresh page to check higher bids.")
            return HttpResponseRedirect(reverse("show_listing", kwargs={"listing_id":listing_id}))
    else:
        return HttpResponse(f"How did you even get here? Are you pasting the url page directly?")
    
@login_required(login_url="/login?s=t")
def new_comment(request):
    if request.method == "POST":
        user = request.user
        listing_id = request.POST["bid_id"]
        listing = Auction_Listing.objects.get(id=listing_id)
        comment_text = request.POST["content"]
        time = now()
        new_comment = Comments(comment_owner = user,
                               comment_listing = listing,
                               comment_text = comment_text,
                               comment_time = time)
        new_comment.save()
        return HttpResponseRedirect(reverse("show_listing", kwargs={"listing_id":listing_id}))
    else:
        return HttpResponse(f"How did you even get here? Are you pasting the url page directly?")
    
@login_required(login_url="/login?s=t")
def close_poll(request):
    if request.method == "POST":
        listing_id = request.POST["bid_id"]
        listing = Auction_Listing.objects.get(id=listing_id)
        highest_price = listing.bid_price
        winning_bid = Bids.objects.filter(Q(bid_listing = listing) & Q(bid_price = highest_price)).first()
        #print(winning_bid)
        bid_winner = winning_bid.bid_owner
        listing.winner = bid_winner
        listing.save()
        return HttpResponseRedirect(reverse("show_listing", kwargs={"listing_id":listing_id}))
    else:
        return HttpResponse(f"How did you even get here? Are you pasting the url page directly?")

@login_required(login_url="/login?s=t")
def add_to_fav(request):
    if request.method == "POST":
        listing_id = request.POST["bid_id"]
        listing = Auction_Listing.objects.get(id=listing_id)
        user = request.user
        user.watchlist.add(listing)
        return HttpResponseRedirect(reverse("show_listing", kwargs={"listing_id":listing_id}))
    else:
        return HttpResponse(f"How did you even get here? Are you pasting the url page directly?")
    
@login_required(login_url="/login?s=t")
def remove_from_fav(request):
    if request.method == "POST":
        listing_id = request.POST["bid_id"]
        listing = Auction_Listing.objects.get(id=listing_id)
        user = request.user
        user.watchlist.remove(listing)
        return HttpResponseRedirect(reverse("show_listing", kwargs={"listing_id":listing_id}))
    else:
        return HttpResponse(f"How did you even get here? Are you pasting the url page directly?")

@login_required(login_url="/login?s=t")
def my_fav(request):
    user = request.user
    return render(request, "auctions/my_favorite.html", {
        "favorites":user.watchlist.all()
    })

def category(request):
    categries = Auction_Listing.objects.values_list('category', flat=True).distinct()
    return render(request,"auctions/category.html",{
        "categories":categries
    })

def deep_category(request,category_name):
    filter_result = Auction_Listing.objects.filter(category = category_name)
    if category_name == "None":
        filter_result = Auction_Listing.objects.filter(category__isnull = True)
    return render(request,"auctions/deep_category.html",{
        "listings":filter_result
    })