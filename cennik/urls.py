from django.urls import path
from . import views

app_name = "cennik"

urlpatterns = [
    path('', views.index),
    path('zabiegi', views.zabiegi)
]