# First_App_Django
dar permisos a entorno :
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

Características:
Autenticación de usuarios y control de acceso basado en roles (administrador, gerente, empleado).
CRUD de productos, categorías y proveedores.
Registro de entradas y salidas de productos del inventario.
Generación de informes y gráficos de ventas y stock.
Posibilidad de añadir notificaciones automáticas cuando el stock de productos esté por debajo de un nivel específico.
Extras:
Uso de Django Celery para tareas en segundo plano, como enviar correos electrónicos de notificación.
Implementación de WebSockets con Django Channels para notificaciones en tiempo real.



run server: python3 manage.py runserver