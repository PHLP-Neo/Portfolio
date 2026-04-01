from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class User(AbstractUser):
    watchlist = models.ManyToManyField('Auction_Listing', related_name="watchedby")
    pass

class Auction_Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    listing_image_link = models.URLField(blank=True, null=True)
    category = models.CharField(blank=True, null=True, max_length=64)
    bid_price= models.IntegerField()
    owner = models.ForeignKey(User, related_name='owner_listings', on_delete=models.CASCADE)
    winner = models.ForeignKey(User, related_name='winner_listings', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.title} is bidding at the price of {self.bid_price}!"

class Bids(models.Model):
    bid_owner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True,)
    bid_listing = models.ForeignKey(Auction_Listing, on_delete=models.CASCADE,blank=True, null=True,)
    bid_price = models.IntegerField(default=0)
    bid_time = models.DateTimeField(default=now())
    def __str__(self):
        return f"{self.bid_time}: {self.bid_owner} placed {self.bid_price} on {self.bid_listing}"
    pass

class Comments(models.Model):
    comment_owner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True,)
    comment_listing = models.ForeignKey(Auction_Listing, on_delete=models.CASCADE,blank=True, null=True,)
    comment_text = models.TextField(default="")
    comment_time = models.DateTimeField(default=now())
    def __str__(self):
        return f"{self.comment_owner}({self.comment_time}): {self.comment_text}"
    pass