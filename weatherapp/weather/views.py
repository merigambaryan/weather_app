import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# функция для определения пределенного шаблона
def index(request):
    appid = '98c1c20d2ceeffc060c367306670aa7a'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    # выбираем все данные из таблицы города
    cities = City.objects.all()

    all_cities = []

    # перебор данных
    for city in cities:
        # узнаем погоду
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        # записываем полученные данные в массив
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    # передаем список в html шаблон
    return render(request, 'weather/index.html', context)
