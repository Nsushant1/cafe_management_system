from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)
    email=models.EmailField()
    def __str__(self):
        return self.name
    
class InventoryItem (models.Model):
    UNITS = [
        ('g', 'Grams'),
        ('kg', 'Kilograms'),
        ('ml', 'Milliliters'),
        ('L', 'Liters'),
        ('unit', 'Unit'),
    ]
    name= models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True ,blank=True)
    quantity=models.FloatField()
    unit=models.CharField(max_length=10,choices=UNITS)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}({self.quantity} {self.unit})"


