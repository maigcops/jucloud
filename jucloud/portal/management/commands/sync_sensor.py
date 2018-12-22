from django.core.management.base import BaseCommand
from jucloud.drivers import sensor

class Command(BaseCommand):

     def handle(self, *args, **options):
         sensor.SensorServer(sensor.SensorHandler)
