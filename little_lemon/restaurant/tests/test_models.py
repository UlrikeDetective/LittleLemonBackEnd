from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_menu_item_str(self):
        item = Menu.objects.create(title="Spaghetti", price=12.50, inventory=10)
        self.assertEqual(str(item), "Spaghetti")
