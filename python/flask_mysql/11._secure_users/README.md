# Secure Users — Flask + MySQL

Aplicación MVC de registro, autenticación y control de acceso. Las contraseñas se guardan exclusivamente como hashes Bcrypt; los datos de conexión y la clave de Flask se leen desde `.env`.

## Requisitos

- Python 3.14
- Pipenv
- MySQL en `localhost` o valores propios en `.env`

## Preparación

1. Crea la base y la tabla ejecutando `flask_app/bd/esquema_loginreg.sql` en MySQL.
2. Revisa los valores de `.env` (no lo subas al repositorio).
3. Instala y ejecuta:

```powershell
pipenv install
pipenv run python server.py
```

Abre `http://127.0.0.1:5000`. El primer visitante verá el formulario de login; usa “Crear una cuenta” para registrarte.

## Variables de entorno

`.env.example` documenta `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`, `SECRET_KEY` y `COOKIE_SECURE`. En producción usa una clave secreta aleatoria propia, contraseñas de base de datos con privilegios mínimos y HTTPS (`COOKIE_SECURE=true`).

## Rutas

| Método | Ruta | Función |
|---|---|---|
| GET | `/` | Formulario de login |
| GET | `/registro` | Formulario de registro |
| POST | `/registrar` | Valida, comprueba email y almacena el hash |
| POST | `/login` | Verifica la contraseña y crea sesión |
| GET | `/dashboard` | Perfil protegido por sesión |
| GET | `/logout` | Limpia la sesión y vuelve al login |

## Seguridad implementada

- Validación backend y regex de email; normalización de email en minúsculas.
- Email único consultado en Python y protegido por índice `UNIQUE` en MySQL.
- Bcrypt para registro y verificación de contraseña; jamás se guarda la contraseña en texto plano.
- Error de login genérico para no revelar si existe el correo.
- ID de usuario únicamente en la sesión Flask; cookies `HttpOnly` y `SameSite=Lax`, y cookie `Secure` configurable para HTTPS.
- Dashboard requiere sesión y vuelve a validar que el usuario siga existiendo.
- Consultas MySQL parametrizadas.

## Estructura

- `flask_app/models/usuario.py`: validación y consultas de Usuario.
- `flask_app/controllers/usuarios.py`: registro, login, autorización y logout.
- `flask_app/templates/`: shell Bootstrap, login, registro y dashboard.
- `resources/ERD/esquema_loginreg.mmd`: fuente del diagrama de la tabla.
