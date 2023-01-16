from django.db import models
from django.forms import ModelForm
from .models import Wizyta


class AppointmentForm(ModelForm):
    class Meta:
        model = Wizyta
        fields = '__all__'
