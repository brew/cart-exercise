from decimal import Decimal


class Cart(object):

    def get_total(self):
        '''Return sum of cart items as a Decimal.'''
        return Decimal(0)


class CartItem(object):

    def get_line_total(self):
        '''Return total as a Decimal.'''
        return Decimal(0)
