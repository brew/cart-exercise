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
        if self.get_item(item) is None:
            cart_item = CartItem(item)
            self.items.append(cart_item)

    def get_item(self, item_name):
        '''Return CartItem who's product corresponses with item_name.'''
        return next((item for item in self.items if item.product == item_name), None)


class CartItem(object):

    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity

    def get_line_total(self):
        '''Return total as a Decimal.'''
        return Decimal(0)
