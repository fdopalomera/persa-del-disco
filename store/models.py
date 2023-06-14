from django.db import models

class ProductCategory(models.Model): #Namespace? Product Category vs Category
    name = models.CharField(max_length=20)

class ProductType(models.Model):
    name = models.varchar(max_length=100)
    product_category_id = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

class Product(models.Model):

    name = models.CharField(max_length=256)
    product_category = models. # Shouldn't be present? 3NF
    product_type = models.ForeignKey # Dependency with category
    price_clp = models.PositiveIntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    def update_stock(self):
        pass

    def get_product(self):
        pass

class Stock(models.Model):
    quantity = models.PositiveSmallIntegerField() # Max 32767 or should use PositiveInegerField?
    cost_clp = models.PositiveIntegerField()

class Order(models.Model):

    order_date = models.DateField()
    status = models.CharField()

class OrderItem(models.Model):

    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveSmallIntegerField()

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(blank=True, defualt='') # Optional
    first_last_name = models.CharField(max_length=100)
    second_last_name = models.CharField(max_length=100)
    email_adress = models.EmailField()
    created_at = models.DateTimeField()



