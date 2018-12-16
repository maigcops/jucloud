from django.shortcuts import render
from portal import models

# Create your views here.

def homepage(request):
    return render(request, 'portal/home.html', {"a":"a"})

def monitor_charts(request):
    return render(request, 'portal/monitor_charts.html', {"a":"a"})

def monitor_data(request):
    sensor = models.Sensor.objects.get(code='0X0000')
    message = models.Message.objects.filter(sensor=sensor).latest("created_at")
    return render(request, 'portal/monitor_data.html', {"resp":message})