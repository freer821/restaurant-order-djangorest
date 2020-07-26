from django.db import models

# Create your models here.
class Order(models.Model):
    order_no = models.CharField(max_length=200, default='', unique=True)
    fee = models.FloatField(default=0)
    content= models.TextField(default='') # json img
    type = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=50, default='')
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.fee = round(self.fee, 2)
        super(Order, self).save(*args, **kwargs)
