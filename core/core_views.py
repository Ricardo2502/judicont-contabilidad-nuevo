
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("""
        <h1>Bienvenido a Judicont Contabilidad</h1>
        <p>Ir al <a href='/contabilidad/cuentas/'>Catálogo de Cuentas</a></p>
    """)
