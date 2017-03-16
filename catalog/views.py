from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def list_products(request, category_slug=None):

    return HttpResponse("Hello, world. You're at the catalog index.")