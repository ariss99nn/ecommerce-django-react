from django.urls import path
from .views import home, agregar_producto

urlpatterns = [
    path('', home, name='home'),
    path('agregar/', agregar_producto, name='agregar_producto'),
]