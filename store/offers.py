from decimal import Decimal


class AbstractOffer(object):
    '''An interface for subclassing Offer classes.'''

    def __init__(self, target_product):
        self.target_product = target_product

    def calculate_line_total(self, cart_item, store, *args):
        '''All subclasses must implement this method, returning a new total
        for the cart_item.'''
        raise NotImplementedError()


class NoOffer(AbstractOffer):
    '''The simplest offer, is no offer at all.'''

    def calculate_line_total(self, cart_item, store, *args):
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

    def calculate_line_total(self, cart_item, store, *args):
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

    def __init__(self, target_product, dependent_product, discount, *args, **kwargs):
        self.dependent_product = dependent_product
        self.discount = discount
        super(DependentDiscountOffer, self).__init__(target_product, *args, **kwargs)

    def calculate_line_total(self, cart_item, store, cart, *args):
        '''Return total for cart_item taking into account the eligible
        discount that may apply in the presence of dependent products in the
        cart.'''
        try:
            dependent_quantity = cart.get_item(self.dependent_product).quantity
        except AttributeError:
            return cart_item.get_line_total(store)
        else:
            # Number of target_product eligible for discount
            eligible_for_discount = min(dependent_quantity, cart_item.quantity)
            # Full price of a single target_product
            single_full_price = store.get_product_price(cart_item.product)
            # Subtotal for eligible target_product before discount.
            eligible_subtotal = eligible_for_discount * single_full_price
            # Total for eligible target_product after discount.
            eligible_total = eligible_subtotal - (eligible_subtotal * self.discount)
            # Total for ineligible target_product
            remainder_total = (cart_item.quantity - eligible_for_discount) * single_full_price

            return eligible_total + remainder_total
