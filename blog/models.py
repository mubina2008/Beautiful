from django.db import models

# Create your models here.

class Pudra(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    bio = models.TextField()


    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.name


class Customers(models.Model):
    name = models.CharField(max_length=50)
    izoh = models.TextField()


    def __str__(self):
        return self.name