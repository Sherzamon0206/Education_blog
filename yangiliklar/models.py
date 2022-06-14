import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=200,blank=True,null=True)
    text = models.TextField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    img1=models.ImageField(upload_to='sherzamon',blank=True,null=True)
    img2= models.ImageField(upload_to='sherzamon', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=55)

    created_data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
   