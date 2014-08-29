from decimal import Decimal


class Cart(object):

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def get_total(self):
        '''Return sum of cart items as a Decimal.'''
        return Decimal(0)

    def add(self, item):
        '''Add an item to the cart.'''
        cart_item = CartItem(item)
        self.items.append(cart_item)


class CartItem(object):

    def __init__(self, product):
        self.product = product

    def get_line_total(self):
        '''Return total as a Decimal.'''
        return Decimal(0)
