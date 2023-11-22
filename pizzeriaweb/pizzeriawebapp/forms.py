from django import forms
from django.contrib.auth.forms import UserCreationForm

MASA_CHOICES = [
    ('Masa fina', 'Masa fina'),
    ('Masa gruesa', 'Masa gruesa'),
    ('Masa integral', 'Masa integral'),
    ('Masa pan', 'Masa pan'),
    ('Masa crujiente', 'Masa crujiente'),
    ('Masa sin-gluten', 'Masa sin-gluten'),
    ('Masa maíz', 'Masa maíz'),
    ('Masa california', 'Masa california'),
    ('Masa francesa', 'Masa francesa'),
]

SALSA_CHOICES = [
    ('Tomate', 'Tomate'),
    ('Pesto', 'Pesto'),
    ('Blanca', 'Blanca'),
    ('Barbacoa', 'Barbacoa'),
    ('Crema de Ajo', 'Crema de Ajo'),
    ('Cebolla Caramelizada', 'Cebolla Caramelizada'),
    ('Salsa de Queso', 'Salsa de Queso'),
    ('Salsa Alfredo', 'Salsa Alfredo'),
    ('Salsa de Champiñones', 'Salsa de Champiñones'),
    ('Salsa de Mostaza', 'Salsa de Mostaza'),
]

TECNICA_CHOICES = [
    ('Horno', 'Horno'),
    ('Parrilla', 'Parrilla'),
    ('Microondas', 'Microondas'),
    ('Freidora', 'Freidora'),
    ('Ahumado', 'Ahumado'),
    ('Cocina Lenta', 'Cocina Lenta'),
    ('Asado', 'Asado'),
    ('Plancha', 'Plancha'),
    ('Fuego Abierto', 'Fuego Abierto'),
    ('Sous Vide', 'Sous Vide'),
]

PRESENTACION_CHOICES = [
    ('Corte Tradicional', 'Corte Tradicional'),
    ('Pizza Entera', 'Pizza Entera'),
    ('Porciones Individuales', 'Porciones Individuales'),
    ('Pizza Calzone', 'Pizza Calzone'),
    ('Pizza Roll', 'Pizza Roll'),
    ('Pizza Familiar', 'Pizza Familiar'),
    ('Pizza Mediana', 'Pizza Mediana'),
    ('Pizza Mini', 'Pizza Mini'),
    ('Pizza Maxi', 'Pizza Maxi'),
    ('Pizza Gigante', 'Pizza Gigante'),
]

MARIDAJE_CHOICES = [
    ('Vino Tinto', 'Vino Tinto'),
    ('Vino Blanco', 'Vino Blanco'),
    ('Cerveza', 'Cerveza'),
    ('Agua Mineral', 'Agua Mineral'),
    ('Refresco', 'Refresco'),
    ('Limonada', 'Limonada'),
    ('Té', 'Té'),
    ('Sidra', 'Sidra'),
    ('Whisky', 'Whisky'),
    ('Cóctel', 'Cóctel'),
]

EXTRA_CHOICES = [
    ('Salsa Picante', 'Salsa Picante'),
    ('Ajo Asado', 'Ajo Asado'),
    ('Queso Azul', 'Queso Azul'),
    ('Aceite de Trufa', 'Aceite de Trufa'),
    ('Huevo', 'Huevo'),
    ('Piña', 'Piña'),
    ('Chiles Rojos', 'Chiles Rojos'),
    ('Nueces', 'Nueces'),
    ('Jalapeños', 'Jalapeños'),
    ('Tomate Secado al Sol', 'Tomate Secado al Sol'),
]

INGREDIENTES_CHOICES = [
    ('Queso', 'Queso'),
    ('Pepperoni', 'Pepperoni'),
    ('Champiñones', 'Champiñones'),
    ('Pimientos', 'Pimientos'),
    ('Aceitunas', 'Aceitunas'),
    ('Pollo', 'Pollo'),
    ('Jamón', 'Jamón'),
    ('Anchoas', 'Anchoas'),
    ('Atún', 'Atún'),
    ('Tomate Cherry', 'Tomate Cherry'),
    ('Mozzarella', 'Mozzarella'),
    ('Albahaca', 'Albahaca'),
    ('Cebolla', 'Cebolla'),
    ('Salchichas', 'Salchichas'),
]

ENTRANTES_CHOICES = [
    ('Ensalada', 'Ensalada'),
    ('Patatas Bravas', 'Patatas Bravas'),
    ('Croquetas', 'Croquetas'),
    ('Calamares a la Romana', 'Calamares a la Romana'),
    ('Queso Fundido', 'Queso Fundido'),
    ('Nachos con Guacamole', 'Nachos con Guacamole'),
]

POSTRES_CHOICES = [
    ('Tiramisú', 'Tiramisú'),
    ('Helado', 'Helado'),
    ('Brownie con Helado', 'Brownie con Helado'),
    ('Frutas de Temporada', 'Frutas de Temporada'),
    ('Coulant de Chocolate', 'Coulant de Chocolate'),
    ('Cheesecake', 'Cheesecake'),
]


class PizzaCreationForm(forms.Form):

    nombre = forms.CharField(max_length=100)
    masa = forms.ChoiceField(choices=MASA_CHOICES)
    salsa = forms.ChoiceField(choices=SALSA_CHOICES)
    ingredientes = forms.MultipleChoiceField(choices=INGREDIENTES_CHOICES, widget=forms.CheckboxSelectMultiple)
    tecnica = forms.ChoiceField(choices=TECNICA_CHOICES)
    presentacion = forms.ChoiceField(choices=PRESENTACION_CHOICES)
    extras = forms.MultipleChoiceField(choices=EXTRA_CHOICES, widget=forms.CheckboxSelectMultiple, required=False)


class UsuarioForms(forms.Form):
    
    usuario = forms.CharField(max_length=100)
    contraseña = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(max_length=100, widget=forms.PasswordInput)
    email = forms.EmailField(max_length=100)
    nombre = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)

    def clean_confirmar_contraseña(self):
        super().clean()
        contraseña = self.cleaned_data.get("contraseña", "")
        confirmar_contraseña = self.cleaned_data["confirmar_contraseña"]
        
        if contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return confirmar_contraseña

class LoginForms(forms.Form):
    
    usuario = forms.CharField(max_length=100)
    contraseña = forms.CharField(max_length=100, widget=forms.PasswordInput)

class MenuForms1(forms.Form):
    Entrante_1 = forms.ChoiceField(choices=ENTRANTES_CHOICES)
    Pizza_1 = forms.ChoiceField(choices=MASA_CHOICES)
    Maridaje_1 = forms.ChoiceField(choices=MARIDAJE_CHOICES)
    Postre_1 = forms.ChoiceField(choices=POSTRES_CHOICES)

class MenuForms2(forms.Form):
    Entrante_1 = forms.ChoiceField(choices=ENTRANTES_CHOICES)
    Entrante_2 = forms.ChoiceField(choices=ENTRANTES_CHOICES)
    Pizza_1 = forms.ChoiceField(choices=MASA_CHOICES)
    Pizza_2 = forms.ChoiceField(choices=MASA_CHOICES)
    Maridaje_1 = forms.ChoiceField(choices=MARIDAJE_CHOICES)
    Maridaje_2 = forms.ChoiceField(choices=MARIDAJE_CHOICES)
    Postre_1 = forms.ChoiceField(choices=POSTRES_CHOICES)
    Postre_2 = forms.ChoiceField(choices=POSTRES_CHOICES)

class MenuForms3(forms.Form):
    Entrante_1 = forms.ChoiceField(choices=ENTRANTES_CHOICES)
    Entrante_2 = forms.ChoiceField(choices=ENTRANTES_CHOICES)
    Entrante_3 = forms.ChoiceField(choices=ENTRANTES_CHOICES)
    Pizza_1 = forms.ChoiceField(choices=MASA_CHOICES)
    Pizza_2 = forms.ChoiceField(choices=MASA_CHOICES)
    Pizza_3 = forms.ChoiceField(choices=MASA_CHOICES)
    Maridaje_1 = forms.ChoiceField(choices=MARIDAJE_CHOICES)
    Maridaje_2 = forms.ChoiceField(choices=MARIDAJE_CHOICES)
    Maridaje_3 = forms.ChoiceField(choices=MARIDAJE_CHOICES)
    Postre_1 = forms.ChoiceField(choices=POSTRES_CHOICES)
    Postre_2 = forms.ChoiceField(choices=POSTRES_CHOICES)
    Postre_3 = forms.ChoiceField(choices=POSTRES_CHOICES)

class MenuForms4(forms.Form):
    Entrante_1 = forms.ChoiceField(choices=ENTRANTES_CHOICES)
    Entrante_2 = forms.ChoiceField(choices=ENTRANTES_CHOICES)
    Entrante_3 = forms.ChoiceField(choices=ENTRANTES_CHOICES)
    Entrante_4 = forms.ChoiceField(choices=ENTRANTES_CHOICES)
    Pizza_1 = forms.ChoiceField(choices=MASA_CHOICES)
    Pizza_2 = forms.ChoiceField(choices=MASA_CHOICES)
    Pizza_3 = forms.ChoiceField(choices=MASA_CHOICES)
    Maridaje_1 = forms.ChoiceField(choices=MARIDAJE_CHOICES)
    Maridaje_2 = forms.ChoiceField(choices=MARIDAJE_CHOICES)
    Maridaje_3 = forms.ChoiceField(choices=MARIDAJE_CHOICES)
    Maridaje_4 = forms.ChoiceField(choices=MARIDAJE_CHOICES)
    Postre_1 = forms.ChoiceField(choices=POSTRES_CHOICES)
    Postre_2 = forms.ChoiceField(choices=POSTRES_CHOICES)
    Postre_3 = forms.ChoiceField(choices=POSTRES_CHOICES)
    Postre_4 = forms.ChoiceField(choices=POSTRES_CHOICES)

class MenuForms5(forms.Form):
    Entrante_1 = forms.ChoiceField(choices=ENTRANTES_CHOICES)
    Pizza_1 = forms.ChoiceField(choices=MASA_CHOICES)
    Maridaje_1 = forms.ChoiceField(choices=MARIDAJE_CHOICES)
    Postre_1 = forms.ChoiceField(choices=POSTRES_CHOICES)