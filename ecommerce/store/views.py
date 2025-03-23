from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def productos(request):
    return render(request, 'productos.html')

@permission_required('store.change_producto', raise_exception=True)
def editar_producto(request):
    return render(request, 'editar_producto.html')
