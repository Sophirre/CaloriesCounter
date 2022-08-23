# Generated by Django 4.1 on 2022-08-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True, help_text='Enter your age'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='height',
            field=models.FloatField(blank=True, help_text='Enter your height'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=15),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='weight',
            field=models.FloatField(blank=True, help_text='Enter your weight'),
        ),
    ]