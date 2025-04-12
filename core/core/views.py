from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido al sistema contable Judicont</h1><p>Ve a <a href='/contabilidad/cuentas/'>Catálogo de cuentas</a></p>")
