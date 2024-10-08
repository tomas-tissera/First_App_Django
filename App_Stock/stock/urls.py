# stock/urls.py
from django.urls import path
from .views import CustomLoginView, admin_dashboard, gerente_dashboard, empleado_dashboard

from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),  # Página principal
    path('login/', CustomLoginView.as_view(), name='login'),  # URL para el inicio de sesión
    path('logout/', views.logout_view, name='logout'),  # URL para cerrar sesión
    path('Admin/dashboard/', admin_dashboard, name='admin_dashboard'),  # Vista para administrador
    path('Gerente/dashboard/', gerente_dashboard, name='gerente_dashboard'),  # Vista para gerente
    path('Empleado/dashboard/', empleado_dashboard, name='empleado_dashboard'),  # Vista para empleado
    # Otras rutas de tu aplicación
]
