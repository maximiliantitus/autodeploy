from django.forms import ModelForm
from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_upload']