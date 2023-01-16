from django.contrib import admin
from .models import Wizyta
from .forms import AppointmentForm


class AppointmentAdmin(admin.ModelAdmin):
    add_form = AppointmentForm
    model = Wizyta
    list_display = ('user', 'doctor', 'day', 'time', 'time_ordered',)
    list_filter = ('user', 'doctor', 'day', 'time', 'time_ordered',)

admin.site.register(Wizyta, AppointmentAdmin)