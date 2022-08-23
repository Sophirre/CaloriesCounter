from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Meal(models.Model):
    name = models.CharField(max_length=24)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name="meals", null=True)
    calories = models.IntegerField(verbose_name='Calories per 100g')
    fats = models.FloatField()
    proteins = models.FloatField()
    carbohydrates = models.FloatField()

    def __str__(self):
        return self.name





