# Secure Users — Flask + MySQL

Aplicación MVC para registrar usuarios, iniciar sesión y proteger un dashboard. Las contraseñas se guardan únicamente como hashes Bcrypt; las credenciales de MySQL y la clave de Flask se leen desde `.env`.

## Requisitos y preparación

- Python 3.14 y Pipenv
- MySQL disponible localmente o en el host indicado en `.env`

1. Ajusta `.env` localmente. **No compartas ni subas ese archivo.**
2. En MySQL, ejecuta `flask_app/bd/esquema_loginreg.sql`.
3. Instala dependencias e inicia la app:

```powershell
pipenv install
pipenv run python server.py
```

Abre `http://127.0.0.1:5000`. Desde “Crear una cuenta” registra el primer usuario. La base de datos de este proyecto se llama `esquema_secure` (también debe coincidir con `DB_NAME` en `.env`). `FLASK_DEBUG=true` activa el depurador de Flask para desarrollo.

## Variables de entorno

`.env.example` contiene `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME=esquema_secure`, `SECRET_KEY` y `COOKIE_SECURE`. En producción define una clave secreta aleatoria propia, una cuenta MySQL de mínimo privilegio, HTTPS y `COOKIE_SECURE=true`. En local, reemplaza `DB_PASSWORD` por la contraseña que realmente acepta tu servidor MySQL; no la compartas en el chat.

## Rutas

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Formulario de inicio de sesión |
| GET | `/registro` | Formulario de registro |
| POST | `/registrar` | Valida, comprueba unicidad y guarda el hash |
| POST | `/login` | Verifica el hash y crea sesión |
| GET | `/dashboard` | Perfil protegido por sesión |
| GET | `/logout` | Limpia la sesión y regresa al login |

## Seguridad implementada

- Campos requeridos, longitud mínima de dos caracteres para nombre/apellido, email con regex y contraseña de al menos ocho caracteres.
- El email se normaliza a minúsculas y se comprueba en el controlador y con una restricción `UNIQUE` en MySQL.
- Bcrypt calcula un hash nuevo al registrar y compara ese hash al iniciar sesión. La contraseña nunca se inserta en texto plano.
- Login responde con el mismo mensaje para correo inexistente y contraseña incorrecta.
- La sesión contiene solo `usuario_id`; después de autenticar se limpia el contenido previo de la sesión.
- El dashboard valida la sesión y vuelve a consultar el usuario. `session.clear()` se usa para el logout.
- Consultas con valores parametrizados; cookie de sesión `HttpOnly`, `SameSite=Lax` y opción `Secure` configurable.
- `.env` está excluido mediante `.gitignore`; `.env.example` contiene solo marcadores.

## Base de datos y ERD

`flask_app/bd/esquema_loginreg.sql` crea `esquema_secure.usuarios`, con `email UNIQUE`, contraseña `VARCHAR(255)` y fechas automáticas. El ERD vectorial está en `resources/ERD/esquema_loginreg.svg` y su fuente editable Mermaid en `resources/ERD/esquema_loginreg.mmd`. El README del curso pide además un PNG; si la entrega lo exige, exporta el SVG a `esquema_loginreg.png`.

Para comprobar el almacenamiento de contraseñas después de registrar un usuario:

```sql
USE esquema_secure;
SELECT id, nombre, email, password FROM usuarios;
```

`password` debe comenzar con un prefijo Bcrypt como `$2b$`, nunca con la contraseña ingresada.

## Preguntas de comprensión

1. **¿Diferencia entre hashing y cifrado?** El hashing es unidireccional y se usa para verificar contraseñas sin recuperarlas; el cifrado puede revertirse con una clave.
2. **¿Por qué no guardar una contraseña en texto plano?** Quien acceda a la base podría leerla y reutilizarla en otros servicios.
3. **¿Qué función cumple Bcrypt?** Genera hashes lentos y salados diseñados para proteger contraseñas almacenadas.
4. **¿Qué hace `generate_password_hash()`?** Calcula un hash Bcrypt con salt para guardar en vez de la contraseña original.
5. **¿Qué hace `check_password_hash()`?** Comprueba si la contraseña ingresada corresponde al hash almacenado.
6. **¿Por qué no guardar el salt manualmente?** Bcrypt incluye el salt y los parámetros del hash en el resultado que luego utiliza para verificar.
7. **¿Qué función cumple `.env`?** Mantiene configuración local sensible fuera del código fuente.
8. **¿Por qué `.env` debe estar en `.gitignore`?** Evita publicar credenciales y claves secretas al repositorio.
9. **¿Qué guardamos en `session`?** El identificador del usuario autenticado, no su contraseña.
10. **¿Qué pasa al entrar a `/dashboard` sin sesión?** La solicitud se redirige al login y se muestra un mensaje.
11. **¿Por qué `UNIQUE` en email?** Para impedir duplicados incluso si dos solicitudes intentan registrar el mismo correo a la vez.
12. **¿Responsabilidad del modelo?** Validar reglas de datos y consultar/guardar usuarios en MySQL.
13. **¿Responsabilidad del controlador?** Coordinar formularios, validación, autenticación, sesión, redirecciones y modelos.
14. **¿Responsabilidad de la plantilla?** Presentar la interfaz HTML y mensajes recibidos, sin implementar lógica de persistencia.

## Archivos principales

- `flask_app/models/usuario.py`: modelo, regex, validación y consultas parametrizadas.
- `flask_app/controllers/usuarios.py`: registro, login, dashboard protegido y logout.
- `flask_app/templates/`: base Bootstrap y vistas de login, registro y dashboard.
- `flask_app/config/mysqlconnection.py`: conexión PyMySQL configurada desde entorno.
- `server.py`: punto de entrada.
