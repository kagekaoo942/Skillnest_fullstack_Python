# Inicio de sesión - Flask y MySQL

Aplicación de registro e inicio de sesión para practicar validaciones, contraseñas con hash y sesiones de Flask.

## Configuración

1. Crea la base de datos ejecutando `bd/esquema_inicio_sesion.sql` en MySQL.
2. Crea una copia de `.env.example` con el nombre `.env` y completa la contraseña de MySQL.
3. Instala las dependencias:

   ```powershell
   pip install -r requirements.txt
   ```

4. Inicia el servidor:

   ```powershell
   python app.py
   ```

Abre `http://127.0.0.1:5000`.

## Rutas

- `GET /`: muestra los formularios de registro e inicio de sesión.
- `POST /registrar`: valida y guarda un usuario con la contraseña hasheada.
- `POST /login`: verifica el correo y la contraseña.
- `GET /success`: página protegida para usuarios autenticados.
- `GET /logout`: elimina la sesión y vuelve al inicio.

El registro valida nombre y apellido con solo letras, correo válido y único, contraseña de mínimo 8 caracteres con una mayúscula y un número, y confirmación coincidente.
