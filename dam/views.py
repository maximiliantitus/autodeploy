from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Image
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from .forms import *

# Create your views here.
def index(request):
    image_objects = Image.objects.all()
    form = ImageForm(request.POST,request.FILES) 
    if request.method == 'POST': 
            if form.is_valid(): 
                Image.objects.create(filename=form.cleaned_data)
                form.save() 
    return render(request, 'dam/index.html',{'image_objects':image_objects, 'form':form})


