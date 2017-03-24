from django.shortcuts import render
from cart.session_cart import Cart
from orders.forms import CreateOrderForm
from orders.models import OrderedProduct


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderedProduct.objects.create(order=order, product=item['product'],
                                              price=item['price'],
                                              quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})

    form = CreateOrderForm()
    return render(request, 'orders/create.html', {'cart': cart,
                                                  'form': form})
