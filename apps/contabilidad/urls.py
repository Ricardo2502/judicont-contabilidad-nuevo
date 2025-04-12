from django.urls import path
from . import views

urlpatterns = [
    path('cuentas/', views.cuentas, name='cuentas'),
    # Elimina o comenta estas hasta que las implementemos
    # path('diario/', views.diario, name='diario'),
    # path('facturas/', views.facturas, name='facturas'),
    # path('formulario104/', views.formulario104, name='formulario104'),
    # path('reportes/', views.reportes, name='reportes'),
]
