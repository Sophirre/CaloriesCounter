import django
import os

import requests
from bs4 import BeautifulSoup

from constants import (PRODUCT_NAME_COLUMN_INDEX,
                       CALORIES_COLUMN_INDEX,
                       PROTEINS_COLUMN_INDEX,
                       FATS_COLUMN_INDEX,
                       CARBOHYDRATES_COLUMN_INDEX, )

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'caloriescounter.settings')
django.setup()

from ccounter_app.models import Category, Meal


proxies = {
    'https': "157.100.12.138:999",
}

URL = "https://health-diet.ru"

r = requests.get(URL + '/table_calorie/', proxies=proxies)
soup = BeautifulSoup(r.text, "lxml")
categories = soup.find_all('a', class_='mzr-tc-group-item-href')


def categories_filler():
    # Creating model objects from categories and multiple addition to database
    Category.objects.bulk_create([Category(name=category.text) for category in categories])


def meal_filler():
    meals = list()
    categories_objects = Category.objects.all()
    for category in categories:
        link = URL + category.get('href')  # Ex. https://health-diet.ru/base_of_food/food_24506/
        r2 = requests.get(link, proxies=proxies)
        soup2 = BeautifulSoup(r2.text, "lxml")
        rows = soup2.find('tbody').find_all('tr')
        print(f'---Collecting meals from category {category.text}---')
        if soup2.find(class_="uk-alert-danger"):  # Finding any errors on page
            continue
        for row in rows:
            try:
                columns = row.find_all('td')
                name = columns[PRODUCT_NAME_COLUMN_INDEX].text
                calories = float(columns[CALORIES_COLUMN_INDEX].text.split(' ')[0].replace(',', '.'))  # 9.8 кКал => 9.8
                proteins = float(columns[PROTEINS_COLUMN_INDEX].text.split(' ')[0].replace(',', '.'))  # 1,8 г => 1.8
                fats = float(columns[FATS_COLUMN_INDEX].text.split(' ')[0].replace(',', '.'))
                carbohydrates = float(columns[CARBOHYDRATES_COLUMN_INDEX].text.split(' ')[0].replace(',', '.'))
                print(f'Name: {name}')
                print(f'Calories: {calories}')
                print(f'Proteins: {proteins}')
                print(f'Fats: {fats}')
                print(f'Carbohydrates: {carbohydrates}')
            except IndexError as e:
                print(e)
                continue
            meals.append(Meal(name=name,
                              category=categories_objects.filter(name=category.text)[0],
                              calories=calories,
                              fats=fats,
                              proteins=proteins,
                              carbohydrates=carbohydrates))
    Meal.objects.bulk_create(meals)


if __name__ == '__main__':
    categories_filler()
    meal_filler()
