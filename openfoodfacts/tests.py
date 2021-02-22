from django.test import TestCase
import unittest.mock as u
from io import StringIO
from django.core.management import call_command
from openfoodfacts.api import Api
from openfoodfacts.productparser import ProductParser

# Create your tests here.

class TestCommand(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass
    
    @u.patch('openfoodfact.management.commands.fill_database.Product')
    @u.patch('openfoodfact.management.commands.fill_database.Product')
    def test_command_fill_database_output(self, CategoryMock, ProductMock):
        CategoryMock.objects.fill_categories.return_value = True
        ProductMock.objects.fill_products.return_value = True
        out = StringIO()
        call_command('fill_database', stdout=out)
        self.assertIn('Commande effectuee avec succès', out.getvalue())