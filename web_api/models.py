from django.db import models

# Create your models here.

class Product(models.Model):
  product_title = models.CharField(max_length = 150, null = False)
  product_price = models.IntegerField(default = 0, null = False)
  product_main_img = models.CharField(max_length = 100, null = False)
  product_description = models.TextField(blank = True)
  product_badge = models.CharField(max_length = 10, null = False)
  product_type = models.IntegerField(null = False, default = 0)

class Festival(models.Model):
  festival_title = models.CharField(max_length = 150, null = False)
  festival_date = models.DateField(blank = True)
  festival_description = models.TextField(blank = True, max_length=60000)
  festival_img = models.JSONField(default = dict)

class Bucket(models.Model):
  user_id = models.CharField(max_length = 20, null = False)
  bucket_list = models.JSONField(default = list)
