from django.forms import ModelForm
from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image_upload', 'thumb_image_upload']