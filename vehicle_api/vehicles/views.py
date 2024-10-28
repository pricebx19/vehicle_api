from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from services.vehicle_service import VehicleService
from vehicles.serializers import VehicleMakeSerializer, VehicleModelSerializer, VehicleTrimSerializer
from vehicles.serializers.vehicle_serializer import VehicleSerializer


class VehicleDetailView(APIView):
    def get(self, request, year, make, model, model_id):
        vehicle_service = VehicleService()
        vehicle = vehicle_service.get_vehicle(year, make, model, model_id)

        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)


class VehicleYearsView(APIView):
    def get(self, request):
        vehicle_service = VehicleService()
        years = vehicle_service.get_years()

        return Response(years)


class VehicleMakesView(APIView):
    def get(self, request, year):
        vehicle_service = VehicleService()
        makes = vehicle_service.get_makes(year)

        serializer = VehicleMakeSerializer(makes, many=True)
        return Response(serializer.data)


class VehicleModelsView(APIView):
    def get(self, request, year, make):
        vehicle_service = VehicleService()
        models = vehicle_service.get_models(year, make)

        serializer = VehicleModelSerializer(models, many=True)
        return Response(serializer.data)


class VehicleTrimsView(APIView):
    def get(self, request, year, make, model):
        vehicle_service = VehicleService()
        trims = vehicle_service.get_trims(year, make, model)

        serializer = VehicleTrimSerializer(trims, many=True)
        return Response(serializer.data)
