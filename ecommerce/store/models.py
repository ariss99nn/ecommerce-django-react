from django.db import models

# Modelo de Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

# Modelo de Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

# Modelo de Carrito
class Carrito(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)

# Modelo de Venta
class Venta(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)