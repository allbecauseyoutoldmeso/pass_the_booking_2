from django.db import models

class Client(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    dob = models.DateField()
    telephone = models.CharField(max_length=200)

    def add_client(self):
        self.save()
