from django.contrib import admin
from .models import Category, Product, ProductAttribute


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    #raw_id_field = ('product',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'image']
    prepopulated_fields = {'slug': ('name', )}
# Модель товара


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}
    inlines = [ProductAttributeInline,]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
