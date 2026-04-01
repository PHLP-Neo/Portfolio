from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    following = models.ManyToManyField("User", related_name="followed_by")

class Post_listing(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    owner = models.ForeignKey("User", related_name='owner_post', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    liked_person = models.ManyToManyField("User", related_name="like_received")

    def __str__(self):
        return f"{self.owner} has posted {self.title}!"
    
    def serialize(self):
        return {
            "owner": self.owner,
            "title": self.title,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "likes": self.likes,
            "likes_from": self.liked_person
        }