from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

# Vista para usuarios autenticados
@login_required
def home(request):
    return HttpResponse("¡Bienvenido! Estás autenticado.")

# Vista solo para administradores
@permission_required('store.add_producto', raise_exception=True)
def agregar_producto(request):
    return HttpResponse("¡Eres administrador! Puedes agregar productos.")
