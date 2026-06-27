# 4. Create a Model Form
# from https://www.geeksforgeeks.org/python/python-uploading-images-in-django/

from django import forms
from .models import ImagePost


class ImagePostForm(forms.ModelForm):
    tag_text = forms.CharField(
        label="Tags",
        required=False,
        help_text="Separate tags with spaces, e.g. tag_1 tag_2 tag_3"
    )

    class Meta:
        model = ImagePost
        fields = ["title", "description", "image"]