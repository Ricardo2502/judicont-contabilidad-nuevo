from django.db import models

class CuentaContable(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[
        ('ACTIVO', 'Activo'),
        ('PASIVO', 'Pasivo'),
        ('PATRIMONIO', 'Patrimonio'),
        ('INGRESO', 'Ingreso'),
        ('GASTO', 'Gasto')
    ])

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Transaccion(models.Model):
    fecha = models.DateField()
    glosa = models.TextField()

    def __str__(self):
        return f"{self.fecha} - {self.glosa}"

class DetalleTransaccion(models.Model):
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(CuentaContable, on_delete=models.CASCADE)
    debe = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    haber = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=13)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    iva_porcentaje = models.DecimalField(max_digits=4, decimal_places=2, choices=[(0, '0%'), (5, '5%'), (15, '15%')])
    total = models.DecimalField(max_digits=10, decimal_places=2)
