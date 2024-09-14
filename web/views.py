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
