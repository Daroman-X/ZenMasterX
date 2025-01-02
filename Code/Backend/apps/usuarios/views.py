from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth import login

from django.urls import reverse_lazy


# Vista para el login
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'   
    redirect_authenticated_user = True  # Redirige a los usuarios ya autenticados
    form_class = AuthenticationForm  # Aquí aseguramos que se use el formulario de login.


    
class InicioUsuario(LoginRequiredMixin,TemplateView):
    template_name = 'usuarios/inicio_usuario.html'