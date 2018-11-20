"""portal URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'portal'

urlpatterns = [
    path('', views.homepage, name='homepage'),
]
