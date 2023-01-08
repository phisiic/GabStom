from django.contrib import admin
from .models import Appointment
from .forms import AppointmentForm


class AppointmentAdmin(admin.ModelAdmin):
    add_form = AppointmentForm
    model = Appointment
    list_display = ('user', 'doctor', 'day', 'time', 'time_ordered',)

admin.site.register(Appointment, AppointmentAdmin)