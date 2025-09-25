from restaurant.models import Menu
from django.test import TestCase

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.object.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")