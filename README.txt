Al momento de hacer django-admin startproject "nombre del proyecto", se va a crear una carpeta con ese nombre de proyecto.
Necesitamos a partir de ahora que el comando del terminal este adentro de ese carpeta. Necesitamos que el comando del terminar este en el mismo nivel del archivo "manage.py" que fue creado automaticamente con el django-admin.

Dentro del nivel de  manage.py indicamos el comando "django-admin startapp app_nombreApp.
Se creara una nueva carpeta con el nombre del app.

Ruta (Urls.py) -> Views.py (que fazer cuando llego al link de la ruta) -> HTML (que debo exibir cuando llegar a esa pagina) 

Dentro de la carpeta del proyecto, ubicamos el archivo urls.py para setear las rutas.
Dentro de la careta de la app, ubicamos el archivo views.py para indicar las views que queremos mostrar


Para poder crear una base da datos, dentro del file models, se crea una clase y se informa que columnas y que tipos de datos queremos.
Usamos el cmomando "python .\manage.py makemigrations" para que Django crea la base de datos y luego "python .\manage.py migrate" para realizar la migracion a esa base de datos. Todo eso, dentro de la carpeta donde esta ubicado el file manage.py

