from django.conf import Settings
import http.client
import json
from datetime import datetime
from web.models import hava,searchForCity

def getCity(city):
  if(city == "favicon.ico"):
    return
  
  
  conn = http.client.HTTPSConnection("api.openweathermap.org")


  url = "/data/2.5/forecast?q="
  api = "&appid=07d4a54a56622b1b0cb8c37cad02941d"

  conn.request("GET", url+city+api)

  res = conn.getresponse()
  data = res.read()

  formatedData = json.loads(data)

  cityName = searchForCity(city_id = 1, city = city)
  cityName.save()

  tempTemperature = formatedData["list"][0]["main"]["temp"] #Anlamsız hata ? ama çalışıyor
  Temperature = round((tempTemperature-273.15), 1)

  ExpectedState = formatedData["list"][0]["weather"][0]["main"]
  Humidity = formatedData["list"][0]["main"]["humidity"]
  Wind = formatedData["list"][0]["wind"]["speed"]
  CreateTime = datetime.now()

  data = hava(city = city, temperature = Temperature, expected_state = ExpectedState, humidity = Humidity, wind = Wind, create_time = CreateTime)
  
  data.save()

  