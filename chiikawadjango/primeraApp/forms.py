from django import forms
import datetime # Importamos datetime para poder validar el rango de fechas
from primeraApp.choices import tamanos
from primeraApp.models import Categoria, Personaje, Producto

class ProductoForm(forms.ModelForm):
    sku = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: CHK-001'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del producto'}))
    
    # 1. Agregamos required=False para que este campo ya no sea obligatorio al guardar[cite: 19]
    descripcion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Breve descripción'}), 
        required=False
    )
    
    tamano = forms.ChoiceField(choices=tamanos, widget=forms.Select(attrs={'class': 'form-select'}))
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 15000'}))
    fecha_lanzamiento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        empty_label="Selecciona una categoría",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    personaje = forms.ModelChoiceField(
        queryset=Personaje.objects.all(),
        empty_label="Selecciona un personaje",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Producto
        fields = '__all__'

    # --- Validaciones Personalizadas (clean) ---

    # 2. Validar que el precio sea mayor que cero (adaptado de la validación de sueldo)[cite: 19]
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        try:
            precio = int(precio)
        except ValueError:
            raise forms.ValidationError("El precio debe ser un número entero.")
        
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return precio

    # 3. Validar que la fecha de lanzamiento esté en un rango lógico[cite: 19]
    def clean_fecha_lanzamiento(self):
        fecha = self.cleaned_data.get('fecha_lanzamiento')
        if fecha:
            fecha_minima = datetime.date(2020, 1, 1) # Año en que se creó Chiikawa aprox.
            fecha_maxima = datetime.date(2026, 12, 31)
            if not (fecha_minima <= fecha <= fecha_maxima):
                raise forms.ValidationError("La fecha de lanzamiento debe estar entre 2020 y 2026.")[cite: 19]
        return fecha

    # 4. Validar que el nombre solo contenga letras y espacios[cite: 19]
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        # Reemplazamos los espacios por nada solo para la validación de isalpha()
        if nombre and not nombre.replace(" ", "").isalpha():
            raise forms.ValidationError("El nombre debe contener solo letras y espacios.")[cite: 19]
        return nombre