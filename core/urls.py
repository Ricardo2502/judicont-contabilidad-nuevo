from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("""
    <html>
        <head><title>Judicont Contabilidad</title></head>
        <body style='text-align:center; font-family:sans-serif; margin-top:100px;'>
            <h1>Bienvenido a Judicont Contabilidad</h1>
            <p>Tu sistema ya está funcionando correctamente.</p>
        </body>
    </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
]
