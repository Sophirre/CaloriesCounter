from django.http import HttpResponse
from django.shortcuts import render
from ccounter_app.models import Meal, Category
from users.models import CustomUser

# Create your views here.


def home_page(req):
    name = CustomUser.first_name
    usr_daily_calories = CustomUser.get_daily_calories()
    usr_daily_water_norm = CustomUser.get_daily_water_norm()
    return render(req, 'ccounter_app/home_page.html', {'name': name, 
                                                       usr_daily_calories: usr_daily_calories,
                                                       usr_daily_water_norm: usr_daily_water_norm
                                                       })
