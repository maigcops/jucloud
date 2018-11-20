from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'portal/home.html', {"a":"a"})

def monitor_charts(request):
    return render(request, 'portal/monitor_charts.html', {"a":"a"})

def monitor_data(request):
    return render(request, 'portal/monitor_data.html', {"a":"a"})