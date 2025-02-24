## Paso 1: Clonar el proyecto

### Puedes hacerlo usando el siguiente comando:
``` bash
 git clone <url-del-repositorio>
```

## Paso 2: Configurar la base de datos en el .env
### Configura tus credenciales para la base de datos en el archivo `.env`:
``` bash
    DATABASE_NAME=quick
    DATABASE_USER=postgres
    DATABASE_PASSWORD=12345
    DATABASE_HOST=host.docker.internal
    DATABASE_PORT=5432
```

## Paso 3: Correr el Docker
### Primero apaga cualquier contenedor en ejecución
``` bash
    docker compose down
```
### Luego construye y levanta los contenedores

``` bash
    docker compose up --build
```

## Paso 4: Correr Migraciones
### Corre las migraciones de Django dentro del contenedor
``` bash
    docker exec -it django_app python manage.py migrate --noinput
```

### Paso 5: Crear superusuario
### Crea un superusuario para acceder al panel de administración
``` bash
    docker-compose exec web python manage.py createsuperuser
```

### Paso 6: Ver la documentación de las APIs
### Ingresa a la siguiente URL para ver la documentación de las APIs realizadas con `drf_yasg`:
#### http://localhost:8000/swagger/
### Inicialmente, usa la API de `/api/token/` ya que todas las APIs requieren autenticación.

#---------------------------------------------------------------------------------------------------

# Información adicional

## Puedes ver la cantidad de queries y el tiempo estimado en los headers con el middleware creado. Los campos son:
### - X-Total-Queries
### - X-Response-Time

## Además, cada vez que se inicia la aplicación, se ejecutan las pruebas automatizadas especificadas en el `docker-compose`.

#---------------------------------------------------------------------------------------------------

# Docker Compose (versión: 3.8)

## El archivo `docker-compose.yml` incluye las siguientes configuraciones para los servicios:
### - Redis
### - Web (Django)
### - Worker (Celery)
### - Tests (Pruebas automatizadas)

``` bash

    version: '3.8'

    services:
    redis:
        image: redis:6
        container_name: redis_cache
        restart: always
        ports:
        - "6379:6379"

    web:
        build: .
        container_name: django_app
        restart: always
        depends_on:
        - redis
        environment:
        - DEBUG=True
        ports:
        - "8000:8000"
        volumes:
        - .:/app
        - reports_volume:/quick/reports
        - uploads_volume:/quick/uploads
        - static_volume:/quick/staticfiles

    worker:
        build: .
        container_name: celery_worker
        restart: always
        depends_on:
        - web
        - redis
        command: celery -A quick worker --loglevel=info
        volumes:
        - .:/app
        - reports_volume:/quick/reports
        - uploads_volume:/quick/uploads
        - static_volume:/quick/staticfiles

    tests:
        build: .
        container_name: django_tests
        command: >
        sh -c "python -m unittest discover -s apps/users/tests &&
                python -m unittest discover -s apps/menu/tests &&
                python -m unittest discover -s apps/orders/tests &&
                python -m unittest discover -s apps/restaurants/tests"

        env_file:
        - .env
        volumes:
        - .:/app

    volumes:
    reports_volume:
    uploads_volume:
    static_volume:
```

## Ejecutar pruebas por módulo
### Si quieres correr pruebas por módulo, puedes usar cualquiera de los siguientes comandos dependiendo de la app que vayas a correr:

``` bash
    docker exec -it django_app python -m unittest discover -s apps/users/tests
    docker exec -it django_app python -m unittest discover -s apps/menu/tests
    docker exec -it django_app python -m unittest discover -s apps/orders/tests
    docker exec -it django_app python -m unittest discover -s apps/restaurants/tests
``` 

#---------------------------------------------------------------------------------------------------

# Carga de usuarios masivos y generador de reportes

## En [http://localhost:8000/swagger/](http://localhost:8000/swagger/) podrás encontrar también la documentación para:
### - Carga masiva de usuarios (limitado a 20 usuarios).
### - Generación de reportes como un S3, donde se ve el estado y se descarga.

## Hay dos opciones para generar los reportes:
### - CSV
### - JSON

### Cuando es un JSON, se especifica en cada URL que es un JSON (en el POST y en los dos GET que aparecen en la documentación).
### Cuando es un CSV, solo se especifica en la URL como un POST. (no es necesario en los GET)

#---------------------------------------------------------------------------------------------------

# Django Filters

### Cada API utilizada en la web tiene `django-filters` con su respectiva ayuda en el diseño para facilitar su uso para los desarrolladores.
