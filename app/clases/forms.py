from django import forms

from clases.models import Clase, Evaluacion, Seccion
from estudiantes.models import Inscripcion, Matricula


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


class SeccionFormulario(forms.ModelForm):
    class Meta:
        model = Seccion
        fields = ['id', 'periodo', 'docente']
        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'periodo': forms.Select(attrs={'class': 'form-select'}),
            'docente': forms.Select(attrs={'class': 'form-control'})
        }


class InscripcionFormulario(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['matricula']
        widgets = {
            'matricula': forms.Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        periodo = kwargs.pop('periodo')
        clase = kwargs.pop('clase')
        super(InscripcionFormulario, self).__init__(*args, **kwargs)
        self.fields['matricula'].queryset = Matricula.objects.filter(
            periodo=periodo).exclude(inscripciones__seccion__clase=clase)
