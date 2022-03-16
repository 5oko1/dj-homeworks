from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1000, blank=True)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE, verbose_name='Датчик')
