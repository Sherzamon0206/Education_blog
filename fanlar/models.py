from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Kurslar(models.Model):
    name=models.CharField(max_length=40,null=True,blank=True)
    description = models.TextField(blank=True, null=True)
    course_duration=models.IntegerField(null=True,blank=True)
    img = models.ImageField(upload_to='sherzamon', null=True, blank=True)
    online_education=models.BooleanField(null=True,default=False)
    time_course=models.IntegerField(null=True,blank=True)
    aim_of_course=models.TextField(null=True,blank=True)
    offline_price = models.IntegerField(null=True, blank=True, default=700000)
    online_price = models.IntegerField(null=True, blank=True, default=700000)
    slug = models.SlugField(null=True,blank=True, unique=True, max_length=125)
    def __str__(self):
        return self.name



class Section(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    name_uz=models.CharField(max_length=200,null=True, blank=True)
    description=models.TextField(blank=True, null=True)

    course=models.ForeignKey(to=Kurslar,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name


# class News(models.Model):
#     title=models.CharField(max_length=200,blank=True,null=True)
#     text = models.TextField(blank=True, null=True)
#     views = models.PositiveIntegerField(default=0)
#     img=models.ImageField(upload_to='sherzamon',blank=True,null=True)










#
#
# class Fanlar(models.Model):
#     title = models.CharField(max_length=150)
#     summary = models.CharField(max_length=200, blank=True)
#     bolim1 = models.CharField(max_length=200, blank=True)
#     bolim2 = models.CharField(max_length=200, blank=True)
#     bolim3 = models.CharField(max_length=200, blank=True)
#     bolim4 = models.CharField(max_length=200, blank=True)
#     bolim5 = models.CharField(max_length=200, blank=True)
#
#     text1 = models.CharField(max_length=200, blank=True)
#     text1_decription = models.TextField(blank=True)
#
#     text2 = models.CharField(max_length=200, blank=True)
#     text2_decription = models.TextField(blank=True)
#
#     text3 = models.CharField(max_length=200, blank=True)
#     text3_decription = models.TextField(blank=True)
#
#     text4 = models.CharField(max_length=200, blank=True)
#     text4_decription = models.TextField(blank=True)
#
#     text5 = models.CharField(max_length=200, blank=True)
#     text5_decription = models.TextField(blank=True)
#
#
#     body = models.TextField()
#     vaqt = models.CharField(max_length=10)
#     photo = models.ImageField(upload_to='media/images/', blank=True)
#     video_file = models.FileField(upload_to='media/video/',blank=True,null=True)
#     date = models.DateTimeField(auto_now_add=True)
#     narx = models.CharField(max_length=200, blank=True)
#
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('fanlar_detail', args=[str(self.id)])
#
class Cantact(models.Model):
    name = models.CharField(max_length=200)
    tell = models.CharField(max_length=13)
    def __str__(self):
        return self.name
#
#

class AboutPage(models.Model):
    photo1 = models.ImageField(upload_to='media/images/', blank=True, null = True)
    photo2 = models.ImageField(upload_to='media/images/', blank=True, null = True)
    photo3 = models.ImageField(upload_to='media/images/', blank=True, null = True)
    title1 = models.TextField(null = True, blank=True)
    body1 = models.TextField(null = True, blank=True)
    video_file = models.TextField(null=True,blank=True)
    title2 = models.TextField(null = True, blank=True)
    body2 = models.TextField(null = True, blank=True)
    summary = models.TextField(null = True, blank=True)
    derector_photo = models.ImageField(upload_to='media/images/', blank=True, null = True)
    derector_name = models.CharField(max_length=255, null = True, blank=True)
    derector_body = models.TextField(null = True, blank=True)

    def __str__(self):
        return self.title1

class Teachers(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to = 'images', null=True, blank=True)
    course = models.ForeignKey(Kurslar, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    facebook = models.CharField(max_length=86, null=True, blank=True)
    instagram = models.CharField(max_length=25, null=True , blank=True)
    telegram = models.CharField(max_length=88, null=True, blank=True)

    def __str__(self):
        return self.full_name

class Registered_students(models.Model):
    name = models.CharField(max_length=125, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    kurs = models.CharField(max_length=145, null=True, blank=True)

    def __str__(self):
        return self.name

