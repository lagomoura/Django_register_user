
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # ruta, view responsable, nombre referencia
    path('', views.home, name="home"),
    path('usuarios/', views.usuarios, name='usuarios'),
]
