from rest_framework import serializers


class VehicleModelSerializer(serializers.Serializer):
    model_make_id = serializers.CharField()
    model_name = serializers.CharField()