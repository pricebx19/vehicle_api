from rest_framework import serializers


class VehicleTrimSerializer(serializers.Serializer):
    model_id = serializers.CharField()
    model_trim = serializers.CharField()