from django import forms


class UsuarioFormulario(forms.Form):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        widget=forms.widgets.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
