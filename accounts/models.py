from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import custommanager
# Create your models here.

class Customuser(AbstractUser):
   username = None
   profile_picture = models.ImageField(upload_to='profile_pic/')
   phone_number = models.CharField(max_length=100)
   no_of_focus = models.CharField(max_length=100)
   email = models.CharField(max_length=100,unique=True)
   bio = models.CharField(max_length=1000 , null=True)
   country = models.CharField(max_length=100, null=True)
   city = models.CharField(max_length=100, null=True)
   age = models.CharField(max_length=100,null=True)
   profession = models.CharField(max_length=100, null=True)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []
   
   objects = custommanager()
   