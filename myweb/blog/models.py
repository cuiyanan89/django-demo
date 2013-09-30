#_*_coding:utf-8_*_

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img_url = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

