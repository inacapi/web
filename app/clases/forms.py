from django import forms
from clases.models import Clase, Evaluacion


class ClaseFormulario(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'semestre': forms.NumberInput(attrs={'class': 'form-control'})
        }


class EvaluacionFormulario(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['numero', 'porcentaje']
        widgets = {
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'porcentaje': forms.NumberInput(attrs={'class': 'form-control'})
        }
