from django import forms
from django.forms import ModelForm

from estudiantes.models import Estudiante, Matricula, Periodo


class DocenteFormulario(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido']
        widgets = {
            'nombre': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.widgets.TextInput(attrs={'class': 'form-control'}),
        }


class EstudianteFormulario(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido']
        widgets = {
            'nombre': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.widgets.TextInput(attrs={'class': 'form-control'}),
        }


class MatriculaFormulario(ModelForm):
    class Meta:
        model = Matricula
        fields = ['id', 'periodo']
        widgets = {
            'id': forms.widgets.NumberInput(attrs={'class': 'form-control'}),
            'periodo': forms.widgets.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        estudiante = kwargs.pop('estudiante')
        super(MatriculaFormulario, self).__init__(*args, **kwargs)
        self.fields['periodo'].queryset = Periodo.objects.exclude(
            id__in=estudiante.matriculas.values_list('periodo_id', flat=True))
