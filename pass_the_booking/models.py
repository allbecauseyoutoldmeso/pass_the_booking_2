from django.db import models

class Client(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    dob = models.DateField()
    telephone = models.CharField(max_length=200)

class Property(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    internet = models.BooleanField()
