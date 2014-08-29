import unittest
from decimal import Decimal

from cart import Cart, CartItem


class CartTest(unittest.TestCase):

    def test_get_total_is_decimal(self):
        '''Cart.get_total returns a Decimal.'''
        cart = Cart()
        self.assertTrue(type(cart.get_total()) is Decimal)


class CartItemTest(unittest.TestCase):

    def test_get_line_total_is_decimal(self):
        '''Cart.get_line_total returns a Decimal.'''
        cartitem = CartItem()
        self.assertTrue(type(cartitem.get_line_total() is Decimal))
