from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class IceCream(models.Model):
    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name