from django.db import models
from catalog.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    city = models.CharField(max_length=80, verbose_name='Город')
    address = models.TextField(verbose_name='Адрес')
    postal_code = models.CharField(max_length=80, verbose_name='Почтовый индекс')
    description = models.CharField(max_length=200, verbose_name='Краткое описание')
    created = models.DateField(verbose_name='Дата оформления заказа', auto_now_add=True)
    updated = models.DateField(verbose_name='Дата последнего обновления', auto_now=True)
    when_paid = models.DateField(verbose_name='Дата оплаты')
    #is_done = models.BooleanField(verbose_name='Исполнено', default=False)

    class Meta:
        ordering = ['created']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, related_name='product', verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order', verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')

    def __str__(self):
        return str(self.id)

    def calculate_total_cost(self):
        return self.price * self.quantity
