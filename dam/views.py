from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from .models import UserImage
from PIL import Image
from .forms import *

# Create your views here.
def index(request):
    image_objects = UserImage.objects.all()
    files = request.FILES.getlist('img')
    if request.method == 'POST' and request.FILES.getlist('img'):
        for f in files: 
            size = (299, 299)
            image_upload = ImageForm(request.POST.getlist('img'),request.FILES.getlist('img'))
            thumb_name = 'dam/static/dam/images/thumb-'+str(f)
            image = Image.open(f)
            thumb_image = image.resize(size,Image.ANTIALIAS)
            thumb_image.save(thumb_name, quality=100)
            new_image = UserImage.objects.create(filename=f,image_upload=f,thumb_image_upload=thumb_name, image_thumbnail=thumb_name)
    return render(request, 'dam/index.html',{'image_objects':image_objects})


def detail(request,id):
    image_objects = UserImage.objects.all()
    image_object = UserImage.objects.get(id=id)
    return render(request, 'dam/detail.html',{'image_objects':image_objects, 'image_object':image_object})


def deleteimage(request,id):
    UserImage.objects.get(id=id).delete()
    return redirect(index)


def downloadimage(request, filename):
    im = Image.open('dam/static/dam/images/'+ filename)
    extension = filename.split(".")
    response = HttpResponse(content_type='application/image')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    try:
        im.save(response,format='JPEG')
    except:
        im.save(response,format='PNG')
    finally:
        im.save(response,format='GIF')
    return response
