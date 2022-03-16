from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, get_object_or_404
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorsSerializer, SingleSensorsSerializer, MeasurementSerializer


class Sensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class SingleSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SingleSensorsSerializer


class Measurements(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, id=self.request.data.get('sensor'))
        return serializer.save(sensor=sensor)
