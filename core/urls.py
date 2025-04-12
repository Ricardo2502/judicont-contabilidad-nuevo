from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contabilidad/', include('apps.contabilidad.urls')),  # 👈 esta línea es CLAVE
]
