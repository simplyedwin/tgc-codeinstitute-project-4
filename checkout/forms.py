
from django import forms
from .models import Order


class OrderedForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('title', 'price', 'datetime_ordered',
                  'qty')
