from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField, models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(max_length=10, default=0)
    quantity = models.IntegerField(default=0)
    