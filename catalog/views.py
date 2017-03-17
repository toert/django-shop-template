from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the catalog index.")

def list_products(request, category_slug=None):
    print(request)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=current_category)
    else:
        current_category = None
        products = Product.objects.all()
    return render(request, 'templates/catalog/list.html', {
                  'category': current_category,
                  'products': products
    })