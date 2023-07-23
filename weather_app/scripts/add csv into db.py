import sys
from pathlib import Path
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather.settings")
django.setup()

from weather_app.models import AllCities

import csv
from tqdm import tqdm

def translate(string):
    from deep_translator import GoogleTranslator

    return GoogleTranslator(source='en', target='ru').translate(string)


all_cities = AllCities()
with open('../all_cities.csv', encoding="utf8") as f:
    reader = csv.reader(f)

    for row in tqdm(reader, total=68845):
        if row[0] != 'city':
            old = AllCities.objects.get(city=row[0],
                                        country=row[2],
                                        country_short=row[1])
            old.city_ru = translate(row[0])
            old.country_ru = translate(row[2])
            old.save()
            # _, created = AllCities.objects.get_or_create(
            #     city=row[0],
            #     country=row[2],
            #     city_ru=translate(row[0]),
            #     country_ru=translate(row[2]),
            #     country_short=row[1]
            # )
