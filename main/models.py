from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class File(models.Model):
    file_name = models.CharField(max_length = 300)
    upload = models.FileField(upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.file_name