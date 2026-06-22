from django.contrib import admin
from .models import ImagePost, Tag, Favorite, Comment

# Register your models here.
admin.site.register(ImagePost)
admin.site.register(Tag)
admin.site.register(Favorite)
admin.site.register(Comment)