from django import forms
from .models import Pizza

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['masa', 'salsa', 'ingredientes', 'tecnica_coccion', 'presentacion', 'maridaje', 'extras']
