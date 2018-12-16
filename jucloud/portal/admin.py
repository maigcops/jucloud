from django.contrib import admin
from portal import models

# Register your models here.

@admin.register(models.Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('en_name', 'cn_name', 'code', 'unit', 'description')

@admin.register(models.FunctionCode)
class FunctionCodeAdmin(admin.ModelAdmin):
    list_display = ('en_name', 'cn_name', 'code', 'description')

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("created_at", "data", "display_data", "sensor")