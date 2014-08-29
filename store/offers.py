
class AbstractOffer(object):
    '''An interface for subclassing Offer classes.'''

    def __init__(self, target_product):
        self.target_product = target_product

    def calculate_line_total(self, cart_item, store):
        '''All subclasses must impliment this method, returning a new total
        for the cart_item.'''
        raise NotImplementedError()


class NoOffer(AbstractOffer):
    '''The simplest offer, is no offer at all.'''

    def calculate_line_total(self, cart_item, store):
        '''Simply return the cart_item.get_line_total.'''
        return cart_item.get_line_total(store)


class BogofOffer(AbstractOffer):
    '''A 'Buy One Get One Free' offer.'''

    def calculate_line_total(self, cart_item, store):
        '''Only charge for the approriate quantity of an item.'''
        quotient, remainder = divmod(cart_item.quantity, 2)
        charge_quantity = quotient + remainder
        return store.get_product_price(cart_item.product) * charge_quantity
