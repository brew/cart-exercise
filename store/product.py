
class ProductStore(object):
    '''A naive store mapping products to prices.'''

    def __init__(self, items):
        '''Expects items in the format:

            items = [
                ('apple', Decimal(0.15)),
                ('ice cream', Decimal(3.49)),
                ('strawberries', Decimal(2.00)),
                ('snickers bar', Decimal(0.70)),
                ...
            ]
        '''
        self.items = items

    def get_product_price(self, product_name):
        '''Return the price corresponding with the passed product_name.'''
        return next((prod[1] for prod in self.items if prod[0] == product_name), None)
