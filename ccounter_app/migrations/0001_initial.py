# Generated by Django 4.1 on 2022-08-07 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('calories', models.IntegerField()),
                ('fat_percent', models.FloatField()),
                ('protein_percent', models.FloatField()),
                ('fiber_percent', models.FloatField()),
                ('cholesterol_percent', models.FloatField()),
                ('carbohydrates_percent', models.FloatField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meals', to='ccounter_app.category')),
            ],
        ),
    ]
