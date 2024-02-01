from typing import ItemsView
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.shortcuts import reverse

# Create your models here.

CATEGORY_CHOICES = (
    ('D', 'Diesel'),
    ('P', 'Petrol'),
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)



    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username