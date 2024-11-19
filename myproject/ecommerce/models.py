from django.db import models
from django.utils.timezone import now


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    order_date = models.DateTimeField(auto_now_add=True)
    
class SimpleOrder(models.Model):
    choices = [
            ('product1', 'Laptop'),
            ('product2', 'Smartphone'),
            ('product3', 'Headphones'),
            ('product4', 'Smartwatch'),
            ('product5', 'Tablet')
    ]
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    product = models.CharField(
        max_length=100,
        choices=choices
    )
    order_date = models.DateTimeField(default=now)
