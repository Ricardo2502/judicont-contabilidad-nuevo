from django.contrib import admin
from django.urls import path, include
from core.views import inicio  # 👈 Importa la vista de inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),  # 👈 Ruta para la página principal
    path('contabilidad/', include('apps.contabilidad.urls')),  # tus módulos
]
