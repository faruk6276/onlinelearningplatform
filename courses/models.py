from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Courses(models.Model):
    cat = (('Development', 'Development'),('Science','Science'),('Bussiness','Bussiness'))
    price = models.FloatField(null=False, blank=False,max_length=8)
    category = models.CharField(null=False, choices=cat, max_length=50)
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    description = models.CharField( max_length=500,null=False,blank=False)
    thumbnail = models.ImageField(
        null=False, default='default-profile-picture.jpg')

