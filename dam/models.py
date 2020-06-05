from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


# Create your models here.


class UserImage(models.Model):
    filename = models.CharField(max_length=300)
    image_thumbnail = models.CharField(max_length=300)
    tags = TaggableManager()
    folder = models.CharField(max_length=100) 
    upload_date = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    file_size = models.CharField(max_length=50)
    notes = models.CharField(max_length=300)
    file_extension =  models.CharField(max_length=10)
    image_upload = models.ImageField(upload_to='images/',blank=True, null=True, default='Style017-1.jpg')
    thumb_image_upload = models.ImageField(upload_to='images/',blank=True, null=True, default='Style017-1.jpg')
    def __str__(self):
        return self.filename

    def index_url(self):
        return reverse('index', kwargs={
            'id':self.id
        })

