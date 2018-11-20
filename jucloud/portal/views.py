from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'portal/home.html', {"a":"a"})