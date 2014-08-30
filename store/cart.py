from decimal import Decimal


class Cart(object):

    def __init__(self, store=None):
        self.items = []
        self.product_store = store

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def get_total(self, offers=None):
        '''
        Return sum of cart items as a Decimal.

        If a list of offer objects is provided, these are applied where
        appropriate when summing cart items. Where multiple offers may apply
        to one cart item, the cheapest is used.
        '''
        totals = []
        for item in self.items:
            # The original line_total without offers applied.
            line_total = item.get_line_total(self.product_store)

            if offers is not None:
                # Apply each offer in turn
                for offer in offers:
                    if offer.target_product == item.product:
                        offer_total = offer.calculate_line_total(item, self.product_store, self)
                        # Retain cheapest total to append to totals list.
                        if offer_total < line_total:
                            line_total = offer_total

            totals.append(line_total)
        return Decimal(sum(totals))

    def add(self, item, quantity=1):
        '''
        Add an item to the cart. Return the cart item.

        Adding an existing item is additive. The quantity will increase on an
        existing item by the amount passed with the quantity parameter.
        '''
        cart_item = self.get_item(item)
        if cart_item is None:
            cart_item = CartItem(item, quantity)
            self.items.append(cart_item)
        else:
            cart_item.quantity += quantity
        return cart_item

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
