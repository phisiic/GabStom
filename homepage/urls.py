from django.urls import path
from . import views

app_name = "homepage"

urlpatterns = [
    path('', views.index, name="homepage"),
    path('403',views.error_403_view, name="error403"),
]