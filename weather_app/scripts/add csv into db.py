import sys
from pathlib import Path
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather.settings")
django.setup()

from weather_app.models import AllCities

import csv

all_cities = AllCities()
with open('../all_cities.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != 'city':
            _, created = AllCities.objects.get_or_create(
                city=row[0],
                country=row[2],
                country_short=row[1]
            )
