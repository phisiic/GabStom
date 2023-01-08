from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Appointment
from accounts.models import User
from django.contrib import messages

@login_required(login_url='accounts:login')
def index(request):
    doctors = User.objects.staff()
    return render(request, 'index-appt.html', {'Doctors': doctors})


@login_required(login_url='accounts:login')
def book_view(request):
    doctors = User.objects.staff()
    if request.method == 'POST':
        day = request.POST['day']
        doctor = request.POST['doctor']
        service = request.POST['service']
        time = request.POST['time']

        if Appointment.objects.all().filter(day=datetime.strptime(day, "%Y-%m-%d"), time=time, doctor=doctor):
            messages.info(request, 'Niepoprawna data - lekarz zajety')
            return redirect('appointments:index')

        if datetime.strptime(day, "%Y-%m-%d") <= datetime.now():
            messages.info(request, 'Niepoprawna data')
            return redirect('appointments:index')
        else:
            appt = Appointment(user=request.user, service=service, day=day, time=time, doctor=doctor)
            appt.save()
            return render(request, 'successful-appt.html', {'day': day, 'time': time, 'service': service, 'doctor': doctor, 'Doctors': doctors})
    else:
        return render(request, 'index-appt.html')
