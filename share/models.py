from django.db import models
from django.contrib.auth.models import User
from main.models import File
# Create your models here.

class UserShare(models.Model):
    from_user = models.CharField(max_length=300)  
    to_user = models.CharField(max_length=300)   
    file_url = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    uploaded_on = models.DateTimeField(auto_now = True)