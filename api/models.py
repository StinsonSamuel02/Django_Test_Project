from django.db import models


# Create your models here.

class Clasification(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    clasification = models.ForeignKey(Clasification, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
