
from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Pizza', price=80, inventory=100)
        Menu.objects.create(title='Burger', price=12, inventory=50)
     
    def test_getall(self):
        client = APIClient()
        response = client.get('/api/menu-items/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
     
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)