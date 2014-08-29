
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
