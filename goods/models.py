from django.db import models

def upload_to(instance, filename):
    return 'files/{filename}'.format(filename=filename)

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, default='')
    content= models.TextField(default='') # json img
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)


class Good(models.Model):
    category = models.ForeignKey(Category, related_name='good', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    price = models.FloatField(default=0)
    content= models.TextField(default='') # json img
    day_limit = models.PositiveIntegerField(default=0) # 日销售上线
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.price = round(self.price, 2)
        super(Good, self).save(*args, **kwargs)



class FileManagement(models.Model):
    name = models.CharField(max_length=200, default='')
    size = models.CharField(max_length=50, default='')
    file = models.FileField(upload_to = upload_to, default="")
    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)
