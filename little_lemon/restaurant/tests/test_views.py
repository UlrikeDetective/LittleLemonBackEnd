from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pizza", price=10.00, inventory=5)

    def test_get_all_menu_items(self):
        response = self.client.get(reverse('api-menu'))  # Adjust this name as per your urls.py
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Pizza")
