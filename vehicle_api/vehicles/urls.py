from django.urls import path
from .views import VehicleYearsView, VehicleMakesView, VehicleModelsView, VehicleTrimsView, VehicleDetailView

urlpatterns = [
    path('years/', VehicleYearsView.as_view(), name='get_vehicle_years'),
    path('makes/<int:year>/', VehicleMakesView.as_view(), name='get_vehicle_makes'),
    path('models/<int:year>/<str:make>/', VehicleModelsView.as_view(), name='get_vehicle_models'),
    path('trims/<int:year>/<str:make>/<str:model>/', VehicleTrimsView.as_view(), name='get_vehicle_trims'),
    path('vehicle/<int:year>/<str:make>/<str:model>/<int:model_id>', VehicleDetailView.as_view(), name='get_vehicle')
]
