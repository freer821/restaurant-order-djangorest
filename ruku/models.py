from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Forecast(models.Model):
    owner = models.ForeignKey(User, related_name='forecast', on_delete=models.CASCADE)
    logistic_code = models.CharField(max_length=50, default="")
    logistic_company = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=200, default="")
    status = models.CharField(max_length=50, default="") # 0: normal, 1: error like expected_num != real_num
    expected_num = models.PositiveIntegerField(default=0)
    real_num = models.PositiveIntegerField(default=0)
    extra = models.TextField(default="") # sender info, comment
    admin_extra = models.TextField(default="") # sn code, cpn code
    arrivedtime = models.DateTimeField(null=True, blank=True)
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)