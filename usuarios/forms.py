from .models import Usuario
from django.forms import ModelForm 
from django import forms

class UsuarioFormulario(ModelForm):
    class Meta:
        model = Usuario
        widgets = {

            'nombre' : forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'contrasena': forms.widgets.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
        fields = '__all__' 