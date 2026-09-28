# Seguidores

Aplicación Flask/MySQL que modela el seguimiento entre usuarios como una relación N:N de una tabla consigo misma.

## Preparación

1. Asegúrate de tener MySQL ejecutándose.
2. Desde esta carpeta instala las dependencias: `pipenv install`.
3. Ejecuta `flask_app/bd/esquema_seguidores.sql` en MySQL Workbench o desde el cliente MySQL. El script crea la base `esquema_seguidores`, las tablas y los datos de muestra; puede volver a ejecutarse sin duplicar esos datos.
4. La conexión usa por defecto `localhost:3306`, el usuario `root` y contraseña vacía, como en la guía de la actividad. Para otra configuración establece `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_USER` y `MYSQL_PASSWORD` en el entorno antes de iniciar Flask.
5. Inicia el servidor con `pipenv run python server.py` y visita <http://127.0.0.1:5000/>.

En PowerShell, por ejemplo:

```powershell
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "tu-clave"
pipenv run python server.py
```

## Convención de la relación

`usuario_id` identifica a la persona seguida y `seguidor_id` identifica a quien la sigue. La ruta `/seguir` recibe ambos IDs mediante POST; la tabla muestra las relaciones mediante un `SELF JOIN` de `usuarios` con alias `u` y `s`.

Consulta [resources/README.md](resources/README.md) para la representación ER y los pasos de creación del archivo Workbench requerido por la actividad.
