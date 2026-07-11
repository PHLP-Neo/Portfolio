from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ImagePost(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    # https://www.geeksforgeeks.org/python/python-uploading-images-in-django/
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
    timestamp = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, blank=True, related_name="liked_images")

    def __str__(self):
        return self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "likes": self.liked_by.count()
        }


class Comment(models.Model):
    post = models.ForeignKey(ImagePost, on_delete=models.CASCADE, related_name="comments")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)