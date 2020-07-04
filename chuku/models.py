from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Chuku(models.Model):
    owner = models.ForeignKey(User, related_name='chuku', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200, default="")
    sn_code = models.CharField(max_length=200, default="")
    status = models.CharField(max_length=50, default="") # 0: normal, 1: error like expected_num != real_num
    type = models.CharField(max_length=50, default="") # 物品类型
    platform = models.CharField(max_length=50, default="")  # 平台
    contact = models.CharField(max_length=50, default="")  # 负责人
    pack_type = models.CharField(max_length=50, default="")  # 纸箱
    pack_content = models.CharField(max_length=150, default="")  # 内物类型

    logistic_type = models.CharField(max_length=50, default="")  # 物流类型
    logistic_code = models.CharField(max_length=50, default="")
    logistic_company = models.CharField(max_length=50, default="")
    num = models.PositiveIntegerField(default=0)
    weight = models.FloatField(null=True, blank=True, default=None) # 毛重KG
    long = models.FloatField(null=True, blank=True, default=None)
    width = models.FloatField(null=True, blank=True, default=None)
    heigh = models.FloatField(null=True, blank=True, default=None)
    fba_code = models.CharField(max_length=50, default="")

    reciever = models.TextField(default="") # json
    comment = models.TextField(default="") # sn code, cpn code
    sendtime = models.DateTimeField(null=True, blank=True, default=None)
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.weight = round(self.weight, 2)
        self.long = round(self.long, 2)
        self.width = round(self.width, 2)
        self.heigh = round(self.heigh, 2)
        super(Chuku, self).save(*args, **kwargs)