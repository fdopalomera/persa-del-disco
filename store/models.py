from django.db import models
from enum import Enum

class Product(models.Model):

    class Category(models.TextChoices):
        AUDIO = "AUDIO"
        VIDEO = "VIDEO"
        MISCELLANEOUS = "MISC"

    class Type(models.TextChoices):
        CD = 'CD'
        DVD = 'DVD'
        BLURAY = 'Blu-ray'
        LP = 'Vinyl LP'

    name = models.CharField(max_length=256)
    category = models.CharField(max_length=5, choices=Category.choices) # Should have a default?
    type = models.CharField(max_length=10, choices=Type.choices) # Dependency with category
    price_clp = models.PositiveIntegerField()
    stock_units = models.PositiveSmallIntegerField() # Max 32767 or should use PositiveInegerField?
    creation_date = models.DateField()
    last_update = models.DateField()

    def update_stock(self):
        pass

class Order(models.Model):

    order_date = models.DateField()
    status = models.CharField()

class OrderItem(models.Model):

    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveSmallIntegerField()

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


