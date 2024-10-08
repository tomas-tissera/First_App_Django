from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Producto
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView

def homepage(request):
    return render(request, 'stock/homepage.html')
class CustomLoginView(LoginView):
    template_name = 'stock/login.html'  # Ruta a tu plantilla de inicio de sesión

    def form_valid(self, form):
        # Lógica que se ejecuta al iniciar sesión correctamente
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            # Redirigir a la página de inicio o a otra página después del inicio de sesión
            return super().form_valid(form)
        else:
            form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
            return self.form_invalid(form)
    
def logout_view(request):
    return LogoutView.as_view()(request)