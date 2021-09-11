# backend_property
# Inicio si ejecuta en Developer
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser -> crea su usuario

# Inicio si Ejecuta desde staging con docker

paso 1 - >docker-compose build
paso 2 - >docker-compose up
paso 3 - >docker-compose ps

copiamos el name del container backend_property_web_1 que obtnemos del paso anterior

paso 4 -> docker rm -f backend_property_web_1 -> abrir una nueva ventana de terminal para ejecutar este comando

paso 5 -> docker-compose run --rm web python manage.py makemigrations -> ejecutar en la ventana antes abierta

paso 6 -> docker-compose run --rm web python manage.py migrate --settings=config.settings.staging -> ejecutar en la ventana antes abierta

paso 8 -> docker-compose run --rm web python manage.py createsuperuser

paso 9 -> docker-compose run --rm --service-ports web -> ejecutar en la ventana antes abierta deja el server corriendo

# Si prueba en productivo en la url https://backend-properties.herokuapp.com/
Credenciales de prueba 
{
  "email": "brayan@hotmail.com",
  "password": "Sl1200mk2."
}
Ya existen 2 tipos de Usuarios personas y empresas y 2 tipos de Propiedades Urbano y Rural en este entorno puede crear prppiedades y utilizar los endpoints


# Para developer y staging

Debe crear Tipos de Usuarios, debe crear tipos de Propiedades con el name Urbano y Rural exactos como los acabo de nombrar luego de esto podra ejecutar los demas endpoints



# Flujo de la aplicacion

1. Signup
2. Login -> Genera un token access_token el cual es tipo Bearer y se coloca para hacer las demas peticiones que necesitan autenticacion 
3. hacer request


# MODELO ERD
![ERProperty](https://user-images.githubusercontent.com/45110746/132963288-681ea43e-c5e9-48e8-b707-e3a4c963b5a9.png)

