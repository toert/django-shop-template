from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from .session_cart import Cart
from .forms import CartAddProductForm


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    #product = get_object_or_404(Product, product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add_product(product_id=product_id,
                         quantity=cleaned_data['quantity'])
    return redirect('cart:open_cart')


#@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    #product = get_object_or_404(Product, id=product_id)
    cart.remove_product_from_cart(product_id)
    return redirect('cart:open_cart')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})