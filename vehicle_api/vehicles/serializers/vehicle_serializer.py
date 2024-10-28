from rest_framework import serializers


class VehicleSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    make = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    vehicle_type = serializers.CharField(max_length=100, required=False)
    size = serializers.CharField(max_length=100, required=False)