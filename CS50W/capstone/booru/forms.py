from django import forms
from .models import ImagePost


class ImagePostForm(forms.ModelForm):
    tag_string = forms.CharField(
        max_length=300,
        required=False,
        help_text="Separate tags with spaces, e.g. cat blue_eyes landscape"
    )

    class Meta:
        model = ImagePost
        fields = ["title", "description", "image"]