from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=80, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.CharField(max_length=200, verbose_name='Краткое описание')
    image = models.ImageField(upload_to='catalog/categories_images/', blank=True, verbose_name='Изображение категории')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='catalog/products_images/%Y/%m/%d/', blank=True, verbose_name='Изображение товара')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='На складе')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = [
            ['id', 'slug']
        ]
    def __str__(self):
        return '{}/{}'.format(self.category, self.name)


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, related_name='attributes', db_index=True, verbose_name='Товар')
    attribute_name = models.CharField(max_length=80, db_index=True, verbose_name='Название характеристики')
    attribute_value = models.CharField(max_length=200, verbose_name='Значение характеристики')

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики Товаров'

    def __str__(self):
        return self.product, self.attribute_name, self.attribute_value
