from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Warehouse(models.Model):
    owner = models.ForeignKey(User, related_name='warehouse', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    unknown_num = models.PositiveIntegerField(default=0) # 待操作 已入库
    normal_num = models.PositiveIntegerField(default=0)
    error0_num = models.PositiveIntegerField(default=0) # 划痕
    error1_num = models.PositiveIntegerField(default=0) # 故障
    isactived = models.BooleanField(default=True)
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)


class WarehouseDetail(models.Model):
    product_name = models.CharField(max_length=200, default="")
    status = models.CharField(max_length=50, default="")
    sn_code = models.CharField(max_length=50, default="")
    descrp = models.TextField(default="")
    operation_time = models.DateTimeField(auto_now=True)