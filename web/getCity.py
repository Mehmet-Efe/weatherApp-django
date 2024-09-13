from django.conf import Settings
import http.client
import json
from datetime import datetime
from web.models import hava
from django.utils import timezone

def getCity(city):
  conn = http.client.HTTPSConnection("api.openweathermap.org")
  print("çalışıyor")

  url = "/data/2.5/forecast?q="
  api = "&appid=07d4a54a56622b1b0cb8c37cad02941d"
  city = "Elazig"

  conn.request("GET", url+city+api)

  res = conn.getresponse()
  data = res.read()

  formatedData = json.loads(data)

  