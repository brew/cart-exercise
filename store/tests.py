import unittest
from decimal import Decimal

from cart import Cart, CartItem


class CartTest(unittest.TestCase):

    def test_get_total_is_decimal(self):
        '''Cart.get_total() returns a Decimal.'''
        cart = Cart()
        self.assertTrue(type(cart.get_total()) is Decimal)

    def test_add_single_item(self):
        '''Cart.add() a single item is successful.'''
        cart = Cart()
        cart.add('apple')
        self.assertEqual(len(cart), 1)

    def test_add_item_is_cartitem(self):
        '''Cart contains a single CartItem after cart.add().'''
        cart = Cart()
        cart.add('apple')
        self.assertTrue(type(cart[0]) is CartItem)

    def test_add_two_items(self):
        '''Adding more than one item increases cart length.'''
        cart = Cart()
        cart.add('apple')
        cart.add('orange')
        self.assertTrue(len(cart), 2)


class CartItemTest(unittest.TestCase):

    def test_get_line_total_is_decimal(self):
        '''Cart.get_line_total() returns a Decimal.'''
        cartitem = CartItem('apple')
        self.assertTrue(type(cartitem.get_line_total() is Decimal))
