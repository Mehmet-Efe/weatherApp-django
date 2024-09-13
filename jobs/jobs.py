from django.conf import Settings
import http.client
import json
from datetime import datetime
from web.models import hava, searchForCity
from django.utils import timezone

def scheduler():
  conn = http.client.HTTPSConnection("api.openweathermap.org")
  print("çalışıyor")

  url = "/data/2.5/forecast?q="
  api = "&appid=07d4a54a56622b1b0cb8c37cad02941d"

  test = hava(city = "Elazığ")
  test.save()

  #city = hava.objects.filter(city_id = 0)
  city = "Elazığ"

  conn.request("GET", url+city+api)

  res = conn.getresponse()
  data = res.read()

  formatedData = json.loads(data)
  
  cityName = formatedData["city"]["name"]
  Temperature = round(formatedData["list"][0]["main"]["temp"]-273.15, 1)
  ExpectedState = formatedData["list"][0]["weather"][0]["main"]
  Humidity = formatedData["list"][0]["main"]["humidity"]
  Wind = formatedData["list"][0]["wind"]["speed"]
  CreateTime = datetime.now()

  data = hava(city = cityName, temperature = Temperature, expected_state = ExpectedState,
              humidity = Humidity, wind = Wind, create_time = CreateTime)
  
  data.save()

  print(cityName)