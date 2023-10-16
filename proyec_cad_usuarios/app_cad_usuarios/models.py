from django.db import models
#. Creacion de una clase para poder guardar un modelo de base de datos. Basicamente idicamos que columnas vamos a querer guardar en nuestra base de datos y que tipos de datos se aceptan
class Usuario(models.Model):
  id_usuario = models.AutoField(primary_key=True)
  nombre = models.TextField(max_length=255)
  email = models.EmailField()
  