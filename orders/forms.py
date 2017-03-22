from django import forms
from orders.models import Order


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order

    fields = ['first_name', 'last_name', 'content', 'email', 'city', 'address', 'postal_code', 'description']

