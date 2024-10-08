from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Producto
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import Group
from django.contrib.auth import logout


def homepage(request):
    return render(request, 'stock/homepage.html')
class CustomLoginView(LoginView):
    template_name = 'stock/login.html'  # Ruta a tu plantilla de inicio de sesión

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)

            # Verificar el grupo del usuario y redirigir según corresponda
            if user.groups.filter(name='Administrador').exists():
                return redirect('admin_dashboard')  # Redirige al dashboard del administrador
            elif user.groups.filter(name='Gerente').exists():
                return redirect('gerente_dashboard')  # Redirige al dashboard del gerente
            elif user.groups.filter(name='Empleado').exists():
                return redirect('empleado_dashboard')  # Redirige al dashboard del empleado
            else:
                return redirect('homepage')  # Redirigir a la página principal si no hay grupo

        else:
            form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
            return self.form_invalid(form)

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('homepage')  # Redirige a la página de inicio de sesión
@login_required  # Asegúrate de que el usuario esté autenticado para acceder a esta vista
def admin_dashboard(request):
    return render(request, 'stock/admin_dashboard.html')  # Plantilla para el dashboard del administrador

@login_required  # Asegúrate de que el usuario esté autenticado para acceder a esta vista
def gerente_dashboard(request):
    return render(request, 'stock/gerente_dashboard.html')  # Plantilla para el dashboard del gerente

@login_required  # Asegúrate de que el usuario esté autenticado para acceder a esta vista
def empleado_dashboard(request):
    return render(request, 'stock/empleado_dashboard.html')  # Plantilla para el dashboard del empleado
