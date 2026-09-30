from django.db import models
from django.utils import timezone
from primeraApp.choices import tamanos # Importado desde tu aplicación existente

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de la Categoría')
    creado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Personaje(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Personaje')
    creado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        db_table = 'personaje'
        verbose_name = 'Personaje'
        verbose_name_plural = 'Personajes'

class Producto(models.Model):
    sku = models.CharField(max_length=20, verbose_name='Código SKU')
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Producto')
    # Hacemos que la descripción sea opcional
    descripcion = models.CharField(max_length=250, verbose_name='Descripción', blank=True, null=True) 
    tamano = models.CharField(max_length=1, choices=tamanos, default='m')
    precio = models.PositiveIntegerField(default=10000, verbose_name='Precio')
    fecha_lanzamiento = models.DateField(blank=True, null=True, verbose_name='Fecha de Lanzamiento')
    
    categoria = models.ForeignKey(Categoria, null=False, on_delete=models.RESTRICT)
    personaje = models.ForeignKey(Personaje, null=True, on_delete=models.CASCADE)
    # Evitamos que Django exija este campo en las validaciones
    creado = models.DateTimeField(default=timezone.now, editable=False) 

    def __str__(self):
        return "{} - {}".format(self.sku, self.nombre)

    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['personaje', 'nombre']
