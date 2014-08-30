import csv
from decimal import Decimal


class NoSuchProductError(Exception):
    pass


class ProductStore(object):

    '''A naive store mapping products to prices.'''

    @classmethod
    def init_from_filepath(cls, filepath):
        '''Return an instance initialized from a CSV file.'''
        with open(filepath, 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            items = []
            for row in csvreader:
                items.append((row[0], Decimal(row[1])))
        return cls(items)

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
        product_price = next((prod[1] for prod in self.items if prod[0] == product_name), None)
        if product_price is None:
            raise NoSuchProductError('No such product "{product_name}" in this store.'.format(product_name=product_name))
        else:
            return product_price
