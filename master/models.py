from django.conf import settings
from django.db import models
from django.utils import timezone
from ecom.models import Users

class Category(models.Model):

    name = models.CharField(max_length=200, null=False)
    admin = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Products(models.Model):

    name = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.TextField()
    price = models.FloatField(null=False)
    admin = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Cart_user(models.Model):

    prod = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    created_date = models.DateTimeField(default=timezone.now)