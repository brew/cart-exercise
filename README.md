Shopping Cart Programming Exercise
===

## ProductStore

Products are stored in a `ProductStore` object. This can either be created from a list of product tuples or initialized from a CSV file.

```python
from decimal import Decimal
from product import ProductStore

products = [
    ('apple', Decimal('0.15')),
    ('ice cream', Decimal('3.49')),
    ('strawberries', Decimal('2.00')),
    ('snickers bar', Decimal('0.70')),
]
product_store = ProductStore(products)

# or

import os

csv_filepath = os.path.abspath('products.csv')
product_store = ProductStore.init_from_filepath(csv_filepath)
```

The price for a product can be retrieved with `get_product_price()`.

```python
price = product_store.get_product_price('strawberries')
```

## Cart

Carts should be created with a ProductStore instance from which the cart can derive prices.

```python
from cart import Cart

my_cart = Cart(product_store)
```

Products can be added to a cart by name, with an optional quantity parameter.

```python
cart.add('apple')
cart.add('strawberries', 3)
```

The total for the cart can be calculated with `get_total()`. This method optionally takes a list of [Offer](#offers) objects that are applied to items in the cart when calculating the total.

```python
total = cart.get_total()

# with offers
total_with_offers = cart.get_total(offers=[offer_one, offer_two, offer_three])
```

## Offers

Offer classes inherit from `AbstractOffer` and must implement the `calculate_line_total()` method.

Three example offer classes are provided; `NoOffer`, `MultiBuyOffer`, and `DependentDiscountOffer`.

### NoOffer

A simple example offer that doesn't affect the target product price.

```python
nooffer_strawberries = NoOffer('strawberries')
```

### MultiBuyOffer

Buy a quantity of a product to receive an additional quantity free. For example, buy one get one free, or, buy two get a third free.

```python
# buy one get one free on strawberries
bogof_strawberries = MultiBuyOffer('strawberries', 1, 1)

# buy two get third free on apples
multibuy_apples = MultiBuyOffer('apple', 2, 1)
```

### DependentDiscountOffer

A discount is applied to the target_product in the presence of another product. For example, get 20% off a Snickers bar if you buy a Mars bar at the same time.

```python
snickers_mars_20_discount = DependentDiscountOffer('snickers bar', 'mars bar', Decimal('0.2'))
```
