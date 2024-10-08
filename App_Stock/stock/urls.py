from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Esta línea define la ruta base

    path('login/', views.CustomLoginView.as_view(), name='login'),  # Agrega la ruta de login
    # Otras rutas de tu aplicación
]