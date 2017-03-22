from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm




def list_products(request, category_slug=None):
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=current_category)
    else:
        current_category = None
        products = Product.objects.all()
    return render(request, 'catalog/list.html', {
                  'category': current_category,
                  'products': products
    })


def render_product_page(request, id, product_slug, category_slug):
    print('Page opened!')
    current_category = get_object_or_404(Category, slug=category_slug)
    current_product = get_object_or_404(Product, id=id, slug=product_slug, category=current_category)
    add_to_cart_form = CartAddProductForm()
    return render(request, 'catalog/product_page.html',
                  {'product': current_product,
                   'cart_form': add_to_cart_form
                   })