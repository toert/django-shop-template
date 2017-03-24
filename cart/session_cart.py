from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from catalog.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add_product(self, product_id, quantity=1):
        product_id = str(product_id)
        price_of_product = get_object_or_404(Product, id=product_id).price
        self.cart[product_id] = {'quantity': quantity,
                                 'price': str(price_of_product),
                                 'total_price': str(price_of_product * quantity)}

        if self.cart[product_id]['quantity'] <= 0:
            del self.cart[product_id]
        self.save_session()

    def remove_product_from_cart(self, product_id):
        del self.cart[str(product_id)]
        self.save_session()

    def save_session(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(product['total_price']) for product in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products_in_cart = Product.objects.filter(id__in=product_ids).all()
        for product in products_in_cart:
            self.cart[str(product.id)]['product'] = product
            yield self.cart[str(product.id)]

    def __len__(self):
        return sum([int(product['quantity']) for product in self.cart.values()])