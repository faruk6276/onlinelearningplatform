from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    g = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
    uid = models.OneToOneField(User, on_delete=models.CASCADE,null=False)
    gender = models.CharField(choices=g, max_length=50,null=True,blank=True)
    profile_picture = models.ImageField(
        default="default-profile-picture.jpg", null=True, blank=True)
    phonenumber = models.CharField(max_length=15, null=True, blank=True)
    date_created = models.DateTimeField(null=True, auto_now_add=True)
    is_teacher = models.BooleanField(default=False)
