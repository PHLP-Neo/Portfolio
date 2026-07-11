from django.contrib import admin
from .models import User, ImagePost, Tag, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(ImagePost)
admin.site.register(Tag)
admin.site.register(Comment)