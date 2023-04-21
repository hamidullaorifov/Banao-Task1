from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='images/')
    email = models.EmailField(max_length=200)
    type = models.CharField(choices=(('patient','Patient'),('doctor','Doctor')),default='patient',max_length=10)
    line1 = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=200,blank=True,null=True)
    state = models.CharField(max_length=200,blank=True,null=True)
    pincode = models.PositiveIntegerField(blank=True,null=True)


    @property
    def picture_url(self):
        if self.profile_picture:
            url=self.profile_picture.url
        else:
            url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRxN-HcCY8vkC5AR8G8QJN6HFOklqleEMQc8KhBtZtnQ&s'
        return url
    
