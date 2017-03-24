from django import forms



PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)


#class CartQuantityProduct(forms.Form):
#    quantity = forms.IntegerField(min_value=0, step=1)