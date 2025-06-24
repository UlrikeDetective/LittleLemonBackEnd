from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework.permissions import AllowAny
from django.urls import reverse

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create some test Menu items
        self.item1 = Menu.objects.create(title="Pasta", price=12.50, inventory=10)
        self.item2 = Menu.objects.create(title="Salad", price=8.00, inventory=5)

    def test_getall(self):
        # Get all menu items via API
        response = self.client.get("/api/menu/")  # or reverse('api-menu') if you named it

        # Serialize the objects manually for comparison
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        # Check the response matches the serialized data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
