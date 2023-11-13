from django.db import models

# Create your models here.

class Account(models.Model):
  user_id = models.CharField(max_length = 20, null = False)
  user_pw = models.CharField(max_length = 200, null = False)
