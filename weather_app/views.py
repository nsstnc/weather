from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import json
import requests

from .models import City, AllCities
from .forms import CityForm
from datetime import datetime
from .history import History

lang = 'ru'  # язык страницы


def get_city_info(city):
    appid = '485c72e0e02b8ec897e58e082634c89d'

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=' + lang + '&cnt=3&appid=' + appid
    res = requests.get(url.format(city)).json()
    # print(res)

    ts = int(res['dt'])
    date_time = datetime.utcfromtimestamp(ts).strftime('%d.%m.%Y %H:%M')

    icon = res["weather"][0]["icon"]

    if icon == '01d':
        background = "clear_sky.mp4"
    elif icon == '01n':
        background = "clear_sky_night.mp4"
    elif icon == '02d':
        background = "few_clouds.mov"
    elif icon == '02n':
        background = "few_clouds_night.mp4"
    elif icon == '03d':
        background = "scattered_clouds.mov"
    elif icon == '03n':
        background = "scattered_clouds_night.mp4"
    elif icon == '04d':
        background = "broken_clouds.mp4"
    elif icon == '04n':
        background = "broken_clouds_night.mp4"
    elif icon == '09d' or icon == '09n':
        background = "shower_rain.mp4"
    elif icon == '10d':
        background = "rain.mp4"
    elif icon == '10n':
        background = "rain_night.mp4"
    elif icon == '11d' or icon == '11n':
        background = "thunderstorm.mp4"
    elif icon == '13d' or icon == '13n':
        background = "snow.mp4"
    elif icon == '50d' or icon == '50n':
        background = "mist.mp4"

    city_info = {
        'city': res['name'],
        'temp': round(res["main"]["temp"]),
        'humidity': res["main"]["humidity"],
        'icon': icon,
        'description': res["weather"][0]["description"],
        'feels_like': round(res['main']['feels_like']),
        'date_time': date_time,
        'background': background,
    }

    return city_info


def clearing(request):
    history = History(request)
    history.clear()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # возврат текущей страницы


def change_lang(request):
    global lang  # работаем с глобальной переменной lang
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':  # является ли запрос AJAXом
        current_lang = request.POST.get('current_lang')  # получаем текущий язык
        if current_lang == 'ru':
            lang = 'en'
        else:
            lang = 'ru'
        return index(request)
    #     return JsonResponse({'data': lang}) # возвращаем измененный язык
    # return JsonResponse({})


def index(request):
    history = History(request)

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        city = form['name'].value()
        history.add(city)
        # if not City.objects.filter(name=city).exists():
        #     form.save()

        context = {
            'info': get_city_info(city),
            'form': form,
            'history': history,
            'lang': lang,
        }
    else:
        background = "few_clouds.mov"

        form = CityForm()
        if lang == 'en':
            form.fields['name'].widget.attrs['placeholder'] = 'Enter a city ...'  # замена placeholder формы при смене языка

        if len(history) > 0:
            city = history.history[0]
            context = {
                'form': form,
                'history': history,
                'info': get_city_info(city),
                'lang': lang,
            }
        else:
            context = {
                'form': form,
                'background': background,
                'lang': lang,
            }

    return render(request, "weather_app/index.html", context)


def search_results(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':  # является ли запрос AJAXом
        res = None
        city = request.POST.get('city')
        if ',' in city:
            town = city.split(',')[0]
            country = city.split(',')[1]
            if len(country) > 0 and country[0] == ' ':
                country = country.replace(' ', '', 1)
            qs = AllCities.objects.filter(city__istartswith=town,
                                          country__istartswith=country).order_by('city')
        else:
            qs = AllCities.objects.filter(city__istartswith=city).order_by('city')
        if len(qs) > 0:
            if len(qs) > 5:
                qs = qs[0:5]
            data = []
            for pos in qs:
                item = {
                    'city': pos.city,
                    'country': pos.country,
                    'country_short': pos.country_short
                }
                data.append(item)
            res = data
        else:
            if lang == 'ru':
                res = 'Города не найдены ...'
            else:
                res = 'No such cities ...'
        return JsonResponse({'data': res})
    return JsonResponse({})
