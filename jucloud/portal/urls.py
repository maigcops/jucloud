"""portal URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'portal'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('monitor/data', views.monitor_data, name='monitor_data'),
    path('monitor/charts', views.monitor_charts, name='monitor_charts'),
]
