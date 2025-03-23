from django.contrib import admin
from .models import Proveedor, Categoria, Producto, Carrito, Venta

admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Venta)