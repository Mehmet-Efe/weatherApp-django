from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
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
    
class jobs(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=25)



@receiver(pre_save,sender=searchForCity)
def startCronJob(sender,instance,**kawgrs):
    
    data = jobs.objects.filter(city_name = instance.city).first()
    if data is None:
        print(f'{instance.city} is added for cron job.')
        data = jobs(city_name = instance.city)
        data.save()
    else:
        print(f'{instance.city} is allready in job list...')
