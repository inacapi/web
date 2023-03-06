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
        codigo_electivo_opuesto = ''
        eliminar_electivo = False

        # Calcular el código del "electivo" opuesto
        if clase.codigo:
            eliminar_electivo = True
            if clase.codigo[4] == '1':
                codigo_electivo_opuesto = clase.codigo[:4] + '2' + clase.codigo[5:]
            else:
                codigo_electivo_opuesto = clase.codigo[:4] + '1' + clase.codigo[5:]

        super(InscripcionFormulario, self).__init__(*args, **kwargs)
        self.fields['matricula'].queryset = Matricula.objects.filter(
            periodo=periodo).exclude(inscripciones__seccion__clase=clase)

        # Eliminar también los que ya están inscritos en el "electivo" opuesto
        if eliminar_electivo:
            self.fields['matricula'].queryset = self.fields['matricula'].queryset.exclude(
                inscripciones__seccion__clase__codigo=codigo_electivo_opuesto)

