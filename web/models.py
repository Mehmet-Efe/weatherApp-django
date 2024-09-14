from django.db import models

# Create your models here.

class hava(models.Model):
    weather_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=25)
    temperature = models.FloatField()
    expected_state = models.CharField(max_length=30)
    humidity = models.FloatField()
    wind = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True)

class searchForCity(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=25)