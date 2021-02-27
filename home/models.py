from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.

class SlideImage(models.Model):
   image = models.FileField(upload_to='slideImage/') 

class PriceList(models.Model):
    product = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.product


class OurWork(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    thumbnail = models.FileField(upload_to='ourWork/')

    def __str__(self):
        return self.title

    def get_name(self):
        return self.title

class OurWorkPhoto(models.Model):
    our_work = models.ForeignKey(OurWork, on_delete=models.CASCADE)
    image_before = models.FileField(upload_to='ourWork/before', null=True, blank=True)
    image_after = models.FileField(upload_to='ourWork/after', null=True, blank=True)

    def __str__(self):
        return self.our_work.get_name()
