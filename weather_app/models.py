from django.db import models

# Create your models here.

class City(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class AllCities(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city_ru = models.CharField(max_length=100, default='')
    country_ru = models.CharField(max_length=100, default='')
    country_short = models.CharField(max_length=10, default='')



