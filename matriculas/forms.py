from .models import Matricula
from django.forms import ModelForm 
from django import forms

class MatriculaFormulario(ModelForm):
    class Meta:
        model = Matricula
        widgets = {

            'id' : forms.widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'periodo': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'estudiante': forms.widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }
        fields = '__all__'