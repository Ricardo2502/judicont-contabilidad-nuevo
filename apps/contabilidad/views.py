from django.shortcuts import render
from django.http import HttpResponse

def cuentas(request):
    return HttpResponse("<h2>Catálogo de Cuentas - En construcción</h2>")

def diario(request):
    return HttpResponse("<h2>Libro Diario - En construcción</h2>")

def facturas(request):
    return HttpResponse("<h2>Facturación Electrónica - En construcción</h2>")

def formulario104(request):
    return HttpResponse("<h2>Formulario 104 SRI - En construcción</h2>")

def reportes(request):
    return HttpResponse("<h2>Reportes Financieros - En construcción</h2>")
