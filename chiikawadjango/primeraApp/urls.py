from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-producto/', views.crear_producto, name='crear_producto'), # Agregamos la ruta del formulario[cite: 12]
]