from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='Pasta', price=25, inventory=10)
        self.assertEqual(str(item), 'Pasta : 25')
