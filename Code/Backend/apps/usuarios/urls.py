from django.urls import path
from apps.usuarios.views import CustomLoginView,InicioUsuario

 
app_name='Usuarios'
urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('inicio/', InicioUsuario.as_view(), name='inicio'),
]
