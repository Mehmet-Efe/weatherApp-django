from datetime import datetime, timedelta
from django.shortcuts import render
from .models import hava
from .getCity import getCity 

# Create your views here.


def main(request):
  return render(request,"web/html/web.html")

def mainRecords(request,city):

  search = hava.objects.filter(city = city).order_by('-create_time')

  getCity(city)

  return render(request,"web/html/web.html",{
    "records": search
  })
  
def allData(request):
  
  data = hava.objects.all().order_by('-create_time')
  
  return render(request,"web/html/web.html", {
    "records": data
  })
  
def lastDay(request,city):
  
  now = datetime.now()
  day = now - timedelta(hours=24)
  
  data = hava.objects.filter(city=city).filter(create_time__gte=day).order_by('-create_time')
  
  return render(request,"web/html/web.html",{
    "records":data
  })
  
def hour(request,city,hour):
  
  now = datetime.now()
  
  time = int(hour)
  
  day = now - timedelta(hours=time)
  
  data = hava.objects.filter(city=city).filter(create_time__gte=day).order_by('-create_time')
  
  return render(request,"web/html/web.html",{
    "records":data
  })