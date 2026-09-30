from django.contrib import admin
from primeraApp.models import Categoria, Personaje, Producto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

class PersonajeAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['sku', 'nombre', 'tamano', 'precio', 'categoria', 'personaje']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Personaje, PersonajeAdmin)
admin.site.register(Producto, ProductoAdmin)