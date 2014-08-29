import unittest
from decimal import Decimal

from cart import Cart


class CartTest(unittest.TestCase):

    def test_get_total_is_decimal(self):
        '''Cart.get_total returns a Decimal.'''
        cart = Cart()
        self.assertTrue(type(cart.get_total()) is Decimal)
