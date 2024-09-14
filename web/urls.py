from django.urls import path
from . import views


urlpatterns = [
    path("", views.main,name="HomePage"),
    path("alldata", views.allData,name="allData"),
    path("oneDay/<str:city>", views.lastDay,name="lastDay"),
    path("hours/<str:city>/<str:hour>", views.hour, name="hour"),
    path("<str:city>",views.mainRecords,name="result")
]