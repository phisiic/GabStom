from django.urls import path
from . import views

app_name = "cennik"

urlpatterns = [
    path('', views.index, name=""),
    path('zabiegi', views.zabiegi)
]