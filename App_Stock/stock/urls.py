# stock/urls.py
from django.urls import path
from .views import CustomLoginView
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', CustomLoginView.as_view(), name='login'),  # URL para el inicio de sesión
    path('logout/', views.logout_view, name='logout'),  # URL para cerrar sesión (asegúrate de definir esta vista)
    # Otras rutas de tu aplicación
]