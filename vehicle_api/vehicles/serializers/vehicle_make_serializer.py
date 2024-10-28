from rest_framework import serializers


class VehicleMakeSerializer(serializers.Serializer):
    make_id = serializers.CharField()
    make_display = serializers.CharField()