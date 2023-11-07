from django.db import models

# Create your models here.

class Account(models.Model):
  user_id = models.CharField(max_length = 20, null = False)
  user_pw = models.CharField(max_length = 60, null = False)

class Product(models.Model):
  product_title = models.CharField(max_length = 150, null = False)
  product_price = models.IntegerField(default = 0, null = False)
  product_main_img = models.CharField(max_length = 100, null = False)
  product_description = models.TextField(blank = True)
  product_badge = models.JSONField(default = "{}")

class Festival(models.Model):
  festival_title = models.CharField(max_length = 150, null = False)
  festival_date = models.DateField(blank = True)
  festival_description = models.TextField(blank = True)
  festival_img = models.JSONField(default = "{}")

class Bucket(models.Model):
  user_id = models.CharField(max_length = 20, null = False)
  bucket_list = models.JSONField(default = "{}")
