from django.db import models

# Create your models here.

class City(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class AllCities(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    country_short = models.CharField(max_length=10, default='')



