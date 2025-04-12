
from django import forms
from apps.contabilidad.models import CuentaContable

class CuentaForm(forms.ModelForm):
    class Meta:
        model = CuentaContable
        fields = ['codigo', 'nombre', 'tipo']
