# API REST de Préstamos – Reto 5

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de una API REST utilizando **Flask**, conectada a una base de datos **MySQL** mediante SQLAlchemy.

La API permite consultar información de los préstamos, buscar registros concretos, filtrar préstamos según su estado de impago, obtener estadísticas generales y realizar consultas a una API externa de códigos postales.

## 2. Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Flask:** desarrollo de la API REST.
- **SQLAlchemy:** conexión y consultas a la base de datos.
- **MySQL:** almacenamiento de los datos.
- **Requests:** comunicación con APIs externas.
- **Docker y Docker Compose:** ejecución y gestión de los servicios.

## 3. Endpoints disponibles

### 3.1. Endpoint principal

| Método | URL | Descripción |
|---|---|---|
| GET | `/` | Comprueba que la API está funcionando. |

### 3.2. Consulta de préstamos

| Método | URL | Descripción |
|---|---|---|
| GET | `/prestamos` | Devuelve los primeros 1.000 préstamos. |
| GET | `/prestamos/<id>` | Busca un préstamo mediante su identificador. |
| GET | `/prestamos/ingresos` | Devuelve los 1.000 préstamos con mayores ingresos. |

### 3.3. Filtros de préstamos

| Método | URL | Descripción |
|---|---|---|
| GET | `/prestamos/impago` | Devuelve hasta 1.000 préstamos con impago. |
| GET | `/prestamos/pago` | Devuelve hasta 1.000 préstamos sin impago. |

### 3.4. Estadísticas

| Método | URL | Descripción |
|---|---|---|
| GET | `/estadisticas` | Devuelve el número total de préstamos, la edad media y los ingresos medios. |

### 3.5. API externa: códigos postales

Se ha integrado la API externa **Zippopotam.us**, que permite obtener información geográfica a partir de un código postal.

| Método | URL | Descripción |
|---|---|---|
| GET | `/codigo_postal/<codigo>` | Consulta la localidad asociada a un código postal español. |

Ejemplo:

`/codigo_postal/48001`

Si el código postal no existe o la API externa no devuelve una respuesta correcta, se devuelve un error 404.

## 4. Base de datos

La API se conecta a una base de datos MySQL mediante SQLAlchemy.

- Base de datos: `creditos`.
- Tabla principal: `clientes_credito`.
- Conexión configurada mediante la variable de entorno `DATABASE_URL`.

La conexión se realiza utilizando las credenciales configuradas en Docker Compose.

## 5. Ejecución del proyecto con Docker

Para ejecutar el proyecto es necesario tener instalado Docker Desktop.

1. Abrir una terminal.
2. Acceder a la carpeta donde se encuentra el archivo `docker-compose.yml`:

```bash
cd docker_reto_5_alumnos
```

3. Ejecutar los servicios:

```bash
docker compose up --build
```

Docker Compose se encarga de iniciar MySQL, cargar los datos y ejecutar la API Flask.

Una vez iniciada, la API estará disponible en:

`http://127.0.0.1:8000/`

## 6. Comprobación de los endpoints

Se puede utilizar el navegador para probar las distintas rutas de la API.

Ejemplos:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/prestamos`
- `http://127.0.0.1:8000/prestamos/1`
- `http://127.0.0.1:8000/prestamos/ingresos`
- `http://127.0.0.1:8000/prestamos/impago`
- `http://127.0.0.1:8000/prestamos/pago`
- `http://127.0.0.1:8000/estadisticas`
- `http://127.0.0.1:8000/codigo_postal/48001`

Todos los endpoints utilizan el método GET y devuelven información en formato JSON.