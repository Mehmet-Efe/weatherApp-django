from django.urls import path
from .views import get_hava,put_hava,getAll,lastDay,hour

urlpatterns = [
    path('all/', getAll, name="getAll"),
    path('change/new/<str:city>', put_hava, name="put_hava"),
    path('lastDay/<str:city>', lastDay, name="lastDay"),
    path('hour/<str:city>/<int:hour>', hour, name="hour"),
    path('<str:city>/', get_hava, name="get_hava"),
]
