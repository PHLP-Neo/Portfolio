from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class ImagePost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/") 
    # ^ https://www.geeksforgeeks.org/python/imagefield-django-models/, no restriction here
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # ^ see assignment 3 - Mail

    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    post = models.ForeignKey(ImagePost, on_delete=models.CASCADE, related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True)
    # ^ see assignment 3 - Mail

    class Meta:
        unique_together = ("user", "post")
    # ^ https://stackoverflow.com/questions/28712848/composite-primary-key-in-django
    # this is to ensure a user can only favorite the same post at most once, so this is like a composite key in concept. you cannot have 2 column of user1 - image1 in the database.

    def __str__(self):
        return f"{self.user.username} favorited {self.post.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(ImagePost, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    # ^ see assignment 3 - Mail

    def __str__(self):
        return f"{self.user.username} on {self.post.title}"