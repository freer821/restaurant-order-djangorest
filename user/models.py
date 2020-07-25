from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    owner = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=50, default="") # mark like delete
    city = models.CharField(max_length=50, default="")
    tel = models.CharField(max_length=30, default="")
    addr = models.CharField(max_length=255, default="")
    updatedtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.username
