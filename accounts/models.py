"""from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class foconeuser(AbstractUser):
  profile_picture = models.ImageField(upload_to="profile")
  phone_number = models.CharField(max_length=100,unique=True)
  email = models.CharField(max_length=100,unique=True)
  otp = models.CharField(max_length=10,null=True)
  is_verified = models.BooleanField(default = False)
  session_duration = models.IntegerField(null=True)
  
  USERNAME_FIELD = 'email'
  """