from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    age = models.IntegerField(help_text="Enter your age", blank=True, null=True)
    sex = models.CharField(max_length=15, choices=[('M', 'Male'), ('F', 'Female')], blank=True, null=True)
    height = models.FloatField(help_text="Enter your height", blank=True, null=True)
    weight = models.FloatField(help_text="Enter your weight", blank=True, null=True)

    #  Harris-Benedict's formula for daily calories calculating
    def get_daily_calories(self):
        return 66.47 + 13.75 * self.weight + 5 * self.height - 6.74 * self.age if self.sex == 'Male' \
                                                else 655.1 + 9.6 * self.weight + 1.85 * self.height - 4.68 * self.age
