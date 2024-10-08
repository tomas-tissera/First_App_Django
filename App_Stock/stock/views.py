from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Producto
from django.contrib.auth.views import LoginView

@login_required
@permission_required('stock.view_producto', raise_exception=True)
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

@login_required
@permission_required('stock.add_producto', raise_exception=True)
def agregar_producto(request):
    # Lógica para agregar producto
    pass

@login_required
@permission_required('stock.change_producto', raise_exception=True)
def editar_producto(request, producto_id):
    # Lógica para editar producto
    pass

@login_required
@permission_required('stock.delete_producto', raise_exception=True)
def eliminar_producto(request, producto_id):
    # Lógica para eliminar producto
    pass

def homepage(request):
    return render(request, 'stock/homepage.html')
class CustomLoginView(LoginView):
    template_name = 'stock/login.html'  # Ruta a tu plantilla de inicio de sesión