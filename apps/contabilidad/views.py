from django.shortcuts import render, redirect
from .models import CuentaContable
from .forms.cuenta_form import CuentaForm

def cuentas(request):
    cuentas = CuentaContable.objects.all().order_by('codigo')
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cuentas')
    else:
        form = CuentaForm()
    return render(request, 'contabilidad/cuentas.html', {'form': form, 'cuentas': cuentas})
