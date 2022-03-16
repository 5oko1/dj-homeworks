from django.urls import path

from measurement.views import SingleSensor, Measurements, Sensors

urlpatterns = [
    path('sensors/', Sensors.as_view()),
    path('sensors/<int:pk>/', SingleSensor.as_view()),
    path('measurements/', Measurements.as_view()),
]
