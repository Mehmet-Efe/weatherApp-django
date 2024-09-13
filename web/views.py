from django.shortcuts import render
from .models import hava
from .getCity import getCity 

# Create your views here.


def main(request):
  return render(request,"web/html/web.html")

def mainRecords(request,city):

  getCity(city)

  search = hava.objects.filter(city = city)

  return render(request,"web/html/web.html",{
    "records":"search"
  })