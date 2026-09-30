from django.shortcuts import render, redirect
from primeraApp.forms import ProductoForm
from primeraApp.models import Producto, Categoria, Personaje

# Tu vista de inicio que ya tenías
def inicio(request):
    return render(request, 'primeraApp/inicio.html')

# --- NUEVA VISTA PARA EL FORMULARIO ---
def crear_producto(request):
    if request.method == 'POST': # Verificamos que corresponda a un POST (envío de datos)
        form = ProductoForm(request.POST) # Recoge los valores del formulario
        if form.is_valid(): # Si cumple con las validaciones[cite: 12]
            form.save() # Guardamos los valores en la base de datos[cite: 12]
            return redirect('inicio') # Redirigimos a la página de inicio al terminar
    else:
        form = ProductoForm() # En caso de ser GET, muestra el formulario vacío[cite: 12]
    
    # Retornamos el formulario para que se dibuje en el template[cite: 12]
    return render(request, 'primeraApp/productoAdd.html', {'form': form})