
class AbstractOffer(object):
    '''An interface for subclassing Offer classes.'''

    def __init__(self, target_product):
        self.target_product = target_product

    def calculate_line_total(self, cart_item, store):
        '''All subclasses must implement this method, returning a new total
        for the cart_item.'''
        raise NotImplementedError()


class NoOffer(AbstractOffer):
    '''The simplest offer, is no offer at all.'''

    def calculate_line_total(self, cart_item, store):
        '''Simply return the cart_item.get_line_total.'''
        return cart_item.get_line_total(store)


class MultiBuyOffer(AbstractOffer):
    '''
    Buy a certain quantity to get another quantity free.

    eg. a Buy One Get One Free offer would look like:
        bogof_offer = MultiBuyOffer(1, 1, 'strawberries')
    and a buy two get one free would look like:
        multibuy_offer = MultiBuyOffer(2, 1, 'strawberries')
    '''

    def __init__(self, target_product, charge_for_quantity, free_quantity, *args, **kwargs):
        self.charge_for_quantity = charge_for_quantity
        self.free_quantity = free_quantity
        super(MultiBuyOffer, self).__init__(target_product, *args, **kwargs)

    def calculate_line_total(self, cart_item, store):
        '''Charge for multiples of the quotient and add remainder.'''
        bundles, remainder = divmod(cart_item.quantity, self.charge_for_quantity + self.free_quantity)
        if remainder > self.charge_for_quantity:
            bundles += 1
            remainder = 0
        charge_quantity = (bundles * self.charge_for_quantity) + remainder
        return store.get_product_price(cart_item.product) * charge_quantity


class DependentDiscountOffer(AbstractOffer):
    '''A percentage discount is applied to the target_product in the presence
    of another product.'''

    def __init__(self, *args, **kwargs):
        super(DependentDiscountOffer, self).__init__(*args, **kwargs)

    def calculate_line_total(self, cart_item, store):
        pass
