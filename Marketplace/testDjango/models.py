from django.db import models


class Company(models.Model):
    company = models.CharField(max_length=30)

    def __set__(self):
        return self.name

class Product(models.Model):
    name_prod = models.CharField(max_length=30)
    description_prod = models.CharField(max_length=255)
    price_prod = models.IntField(max_length=1000000)

    def __set__(self):
        return self.name


