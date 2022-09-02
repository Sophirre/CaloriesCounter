from django.http import HttpResponse
from django.shortcuts import render
from ccounter_app.models import Meal, Category
from users.models import CustomUser

# Create your views here.


def home_page(req):
    return render(req, 'home_page.html')
