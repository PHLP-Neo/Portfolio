# 4. Create a Model Form
# from https://www.geeksforgeeks.org/python/python-uploading-images-in-django/

from django import forms
from .models import ImagePost


class ImagePostForm(forms.ModelForm):
    tag_text = forms.CharField(
        required=False,
        help_text="Separate tags with spaces, e.g. cat blue_eyes landscape"
    )

    class Meta:
        model = ImagePost
        fields = ["title", "description", "image"]