
from django.http import HttpResponse
import os

def inicio(request):
    # Ejecutar migraciones si no se ha hecho aún
    if not os.path.exists("migrated.txt"):
        try:
            import run_migrate
            open("migrated.txt", "w").close()
        except Exception as e:
            print("Error al migrar:", e)

    return HttpResponse("""
        <h1>Bienvenido a Judicont Contabilidad</h1>
        <p>Ir al <a href='/contabilidad/cuentas/'>Catálogo de Cuentas</a></p>
    """)
