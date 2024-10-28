import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from unittest.mock import patch
from services.vehicle_service import VehicleService


@pytest.mark.django_db
class TestVehicleAPIViews:

    def setup_method(self):
        self.client = APIClient()

    @patch.object(VehicleService, 'get_years')
    def test_vehicle_years_view(self, mock_get_years):
        # Mock the VehicleService.get_years method
        mock_get_years.return_value = [2000, 2022]

        # Call the API
        url = reverse('get_vehicle_years')
        response = self.client.get(url)

        # Assert status code and response content
        assert response.status_code == 200
        assert response.json() == {
            'min_year': 2000,
            'max_year': 2022
        }
        mock_get_years.assert_called_once()

    @patch.object(VehicleService, 'get_makes')
    def test_vehicle_makes_view(self, mock_get_makes):
        # Mock the VehicleService.get_makes method
        mock_get_makes.return_value = [
            {'make_id': 'ford', 'make_display': 'Ford'},
            {'make_id': 'toyota', 'make_display': 'Toyota'}
        ]

        # Call the API
        url = reverse('get_vehicle_makes', args=[2022])
        response = self.client.get(url)

        # Assert status code and response content
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]['make_id'] == 'ford'
        assert response.json()[0]['make_display'] == 'Ford'
        mock_get_makes.assert_called_once_with(2022)

    @patch.object(VehicleService, 'get_models')
    def test_vehicle_models_view(self, mock_get_models):
        # Mock the VehicleService.get_models method
        mock_get_models.return_value = [
            {'model_make_id': 'mustang', 'model_name': 'Mustang'},
            {'model_make_id': 'focus', 'model_name': 'Focus'}
        ]

        # Call the API
        url = reverse('get_vehicle_models', args=[2022, 'Ford'])
        response = self.client.get(url)

        # Assert status code and response content
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]['model_make_id'] == 'mustang'
        assert response.json()[0]['model_name'] == 'Mustang'
        mock_get_models.assert_called_once_with(2022, 'Ford')

    @patch.object(VehicleService, 'get_trims')
    def test_vehicle_trims_view(self, mock_get_trims):
        # Mock the VehicleService.get_trims method
        mock_get_trims.return_value = [
            {'model_id': 'mustang_eco', 'model_trim': 'EcoBoost'},
            {'model_id': 'mustang_gt', 'model_trim': 'GT'}
        ]

        # Call the API
        url = reverse('get_vehicle_trims', args=[2022, 'Ford', 'Mustang'])
        response = self.client.get(url)

        # Assert status code and response content
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]['model_id'] == 'mustang_eco'
        assert response.json()[0]['model_trim'] == 'EcoBoost'
        mock_get_trims.assert_called_once_with(2022, 'Ford', 'Mustang')


import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
class TestVehicleAPIIntegration:

    def setup_method(self):
        self.client = APIClient()

    def test_vehicle_years_view(self):
        """Test getting the vehicle years without mocking"""
        url = reverse('get_vehicle_years')
        response = self.client.get(url)

        # Assert status code and check the response structure
        assert response.status_code == 200
        json_data = response.json()
        assert 'min_year' in json_data
        assert 'max_year' in json_data
        assert json_data['min_year'] <= json_data['max_year']

    def test_vehicle_makes_view(self):
        """Test getting vehicle makes for a given year"""
        url = reverse('get_vehicle_makes', args=[2022])
        response = self.client.get(url)

        # Assert status code and check the response structure
        assert response.status_code == 200
        json_data = response.json()
        assert len(json_data) > 0  # Check that makes are returned
        assert 'make_id' in json_data[0]
        assert 'make_display' in json_data[0]

    def test_vehicle_models_view(self):
        """Test getting vehicle models for a given year and make"""
        url = reverse('get_vehicle_models', args=[2022, 'ford'])
        response = self.client.get(url)

        # Assert status code and check the response structure
        assert response.status_code == 200
        json_data = response.json()
        assert len(json_data) > 0  # Check that models are returned
        assert 'model_make_id' in json_data[0]
        assert 'model_name' in json_data[0]

    def test_vehicle_trims_view(self):
        """Test getting vehicle trims for a given year, make, and model"""
        url = reverse('get_vehicle_trims', args=[2022, 'Ford', 'Mustang'])
        response = self.client.get(url)

        # Assert status code and check the response structure
        assert response.status_code == 200
        json_data = response.json()
        assert len(json_data) > 0  # Check that trims are returned
        assert 'model_id' in json_data[0]
        assert 'model_trim' in json_data[0]
