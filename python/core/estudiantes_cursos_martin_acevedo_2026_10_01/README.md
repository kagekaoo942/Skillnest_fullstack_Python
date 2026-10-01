# Estudiantes y Cursos — Core

Aplicación Flask con Jinja2, Bootstrap 5 y MySQL para practicar MVC y una relación 1:N entre cursos y estudiantes.

## Preparación

1. Instala Pipenv y MySQL si todavía no están disponibles.
2. Desde esta carpeta ejecuta `pipenv install`.
3. Revisa `.env` (se incluye localmente con `root` y `1234`; el archivo está excluido de Git) o copia `.env.example` y ajusta las credenciales.
4. En MySQL Workbench, ejecuta `flask_app/bd/esquema_estudiantes_cursos.sql` para crear la base, las tablas y los datos iniciales.
5. Inicia la aplicación con `pipenv run python server.py`.
6. Abre `http://127.0.0.1:5000/`.

## Rutas

| Método | Ruta | Función |
| --- | --- | --- |
| GET | `/` | Redirige a cursos |
| GET | `/cursos` | Lista y permite crear cursos |
| POST | `/cursos/crear` | Guarda un curso |
| GET | `/cursos/<id>` | Muestra el curso y sus estudiantes |
| GET | `/estudiantes/nuevo` | Muestra el formulario de estudiante |
| POST | `/estudiantes/crear` | Guarda un estudiante con su `curso_id` |

El detalle usa `LEFT JOIN`, así que un curso sin estudiantes sigue apareciendo. El diagrama visual y las instrucciones para guardar el ERD nativo `.mwb` están en `resources/README.md`.
