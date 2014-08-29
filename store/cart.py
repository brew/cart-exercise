from decimal import Decimal


class Cart(object):

    def __init__(self, store=None):
        self.items = []
        self.product_store = store

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def get_total(self):
        '''Return sum of cart items as a Decimal.'''
        return Decimal(sum([item.get_line_total(self.product_store) for item in self.items]))

    def add(self, item, quantity=1):
        '''Add an item to the cart.'''
        cart_item = self.get_item(item)
        if cart_item is None:
            cart_item = CartItem(item, quantity)
            self.items.append(cart_item)
        else:
            cart_item.quantity += quantity

    def get_item(self, item_name):
        '''Return CartItem where product corresponds with item_name.'''
        return next((item for item in self.items if item.product == item_name), None)


class CartItem(object):

    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity

    def get_line_total(self, store):
        '''Return total derived from product in store.'''
        return store.get_product_price(self.product) * self.quantity
