from django.urls import path
from . import views


urlpatterns = [
    path("", views.main,name="HomePage"),
    path("<str:city>",views.mainRecords,name="result")
]