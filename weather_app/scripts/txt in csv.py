from googletrans import Translator
from tqdm import tqdm
import pandas as pd
from threading import Thread


def get_city(city):
    import requests
    appid = '485c72e0e02b8ec897e58e082634c89d'

    url = 'http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid=' + appid
    try:
        return requests.get(url.format(city)).json()[0]['local_names']['ru']
    except:
        print(f'Не удалось найти {city}')
        return Translator().translate(text=city, src='en', dest='ru').text


translator = Translator()
file = open('all_cities.txt')
f = [x.strip() for x in file]

# f.readline()

df = pd.DataFrame(columns=['city', 'country'])

for i in tqdm(range(len(f))):
    s = f[i].split(',')
    city = get_city(s[0])
    country = translator.translate(text=s[1], dest='ru', src='en').text
    df.loc[len(df)] = {'city': city, 'country': country}


df.to_csv('all_cities_ru.csv', index=False)
df.to_excel('all_cities_ru.xlsx', index=False)
