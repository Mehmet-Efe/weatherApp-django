from datetime import datetime, timedelta
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from web.models import hava,searchForCity
from .serializer import havaSerializer,schedulerChange

# Create your views here.


@api_view(['GET'])
def getAll(request):
    print("GET ALL")
    durum = hava.objects.all()
    serializer = havaSerializer(durum, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_hava(request,city):
    print("get_hava")
    durum = hava.objects.filter(city=city)
    serializer = havaSerializer(durum, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def put_hava(request):
    """
    durum = searchForCity.objects.get(city_id=1)
    
    serializer = schedulerChange(durum,city)//?????????????
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    print(serializer.data)
    return Response(status = status.HTTP_400_BAD_REQUEST)
    """
    #Syntax = http://127.0.0.1:8000/api/change/new/?city=Adana
    print("put_hava")
    city=request.query_params["city"]
    cityName = searchForCity(city_id = 1, city = city)
    cityName.save()
    return Response(status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def lastDay(request,city):
    print("lastDay")
    now = datetime.now()
    day = now - timedelta(hours=24)
    data = hava.objects.filter(city=city).filter(create_time__gte=day).order_by('-create_time')
    
    serializer = havaSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def hour(request,city,hour):
    print("hour")
    now = datetime.now()
    day = now - timedelta(hours=hour)
    data = hava.objects.filter(city=city).filter(create_time__gte=day).order_by('-create_time')
    
    serializer = havaSerializer(data, many=True)
    return Response(serializer.data)