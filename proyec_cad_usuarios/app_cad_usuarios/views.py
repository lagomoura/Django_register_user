from django.shortcuts import render
from .models import Usuario
from django.core.exceptions import ValidationError
from django.http import HttpResponse


def validar_email(email):
    if not email.endswith('.com'):
        raise ValidationError('Debes insertar un correo válido')


def validar_nombre(nombre):
    if len(nombre) < 3:
        raise ValidationError("El nombre debe contener minimo 3 caracteres")


def home(request):
    return render(request, "usuarios/home.html")


def usuarios(request):
    #! Salvando datos de nuevos usuarios para el BD
    if request.method == "POST":

        nuevo_usuario = Usuario()

        # . Buscando informacion que esta en la pantalla (form) y enviando (POST) a lo que le esta haciendo el request
        nuevo_usuario.nombre = request.POST.get("nombre")
        nuevo_usuario.email = request.POST.get("email")

        email = nuevo_usuario.email
        try:
            validar_email(email)
        except ValidationError:
            return HttpResponse("Favor, ingresar un email válido")

        nombre = nuevo_usuario.nombre
        try:
            validar_nombre(nombre)
        except ValidationError:
            return HttpResponse("Favor, ingresar un nombre válido")

        nuevo_usuario.save()
        #! Exibiendo usuarios registrados en una nueva pagina (en diccionario)
        usuarios = {
            # . Busca todas las informaciones guardadas en la BD
            "usuarios": Usuario.objects.all()
        }
    #! Retornando datos a la pagina de lista_usuarios
    # . Retorna una renderizacion haciendo el request de la url pasada y en la url, indicamos a que archivo html queremos renderizar y pasamos un atributo para ser usado en ese html.
    return render(request, 'usuarios/usuarios.html', usuarios)
