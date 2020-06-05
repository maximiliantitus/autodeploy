from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import UserImage
from PIL import Image
from .forms import *

# Create your views here.
def index(request):
    image_objects = UserImage.objects.all()
    if request.method == 'POST' and request.FILES['img']:
        myfile = request.FILES['img'] 
        size = (299, 299)
        image_upload = ImageForm(request.POST.get('img'),request.FILES.get('img'))
        thumb_name = 'dam/static/dam/images/thumb-'+str(myfile)
        image = Image.open(myfile)
        thumb_image = image.resize(size,Image.ANTIALIAS)
        thumb_image.save(thumb_name, quality=100)
        new_image = UserImage.objects.create(filename=myfile,image_upload=myfile,thumb_image_upload=thumb_name, image_thumbnail=thumb_name)
    return render(request, 'dam/index.html',{'image_objects':image_objects})


