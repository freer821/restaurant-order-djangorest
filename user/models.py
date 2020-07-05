from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    owner = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=50, default="") # mark like delete
    company_name = models.CharField(max_length=50, default="")
    company_tel = models.CharField(max_length=30, default="")
    company_addr = models.CharField(max_length=255, default="")
    updatedtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.username


class FileManagement(models.Model):
    owner = models.ForeignKey(User, related_name='filemanagement', on_delete=models.CASCADE)
    notes = models.CharField(max_length=200, default='')
    file = models.FileField(blank=True, default='')
