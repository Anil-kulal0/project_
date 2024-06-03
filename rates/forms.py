from django import forms
from .models import City

class LogisticsForm(forms.Form):
      from_city = forms.ModelChoiceField(queryset=City.objects.all(), label="From City")
      to_city = forms.ModelChoiceField(queryset=City.objects.all(), label="To City")
      kg = forms.DecimalField(max_digits=10, decimal_places=2, label="KG")
