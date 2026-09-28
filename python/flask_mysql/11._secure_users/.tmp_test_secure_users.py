import ast
import os
from pathlib import Path
from types import SimpleNamespace

from flask_app import app, bcrypt
from flask_app.models.usuario import EMAIL_REGEX, Usuario
import server  # Routes are registered on app import.

root = Path(__file__).parent
python_files = [root / "server.py", *root.joinpath("flask_app").rglob("*.py")]
for source_file in python_files:
    ast.parse(source_file.read_text(encoding="utf-8"), filename=str(source_file))
for name in ("base.html", "login.html", "registro.html", "dashboard.html"):
    app.jinja_env.get_template(name)

assert app.secret_key
assert app.config["SESSION_COOKIE_HTTPONLY"] is True
assert app.config["SESSION_COOKIE_SAMESITE"] == "Lax"
assert EMAIL_REGEX.match("ana.lopez+test@example.co.uk")
assert not EMAIL_REGEX.match("ana@example")
assert "SECRET_KEY" in os.environ
assert ".env" in (root / ".gitignore").read_text(encoding="utf-8")

accounts = {}
saved_payloads = []
save_calls = []
checks = []


def user_from_record(record):
    return SimpleNamespace(**record)


def fake_email_exists(cls, data):
    return data["email"] in accounts


def fake_save(cls, data):
    save_calls.append(data.copy())
    if data.get("password") == "__DB_ERROR__":
        return False
    user_id = len(accounts) + 1
    record = {
        "id": user_id,
        "nombre": data["nombre"],
        "apellido": data["apellido"],
        "email": data["email"],
        "password": data["password"],
        "created_at": None,
        "updated_at": None,
    }
    accounts[data["email"]] = record
    saved_payloads.append(data.copy())
    return user_id


def fake_find_email(cls, data):
    record = accounts.get(data["email"])
    return user_from_record(record) if record else None


def fake_find_id(cls, data):
    record = next((row for row in accounts.values() if row["id"] == data["id"]), None)
    return user_from_record(record) if record else None


Usuario.existe_email = classmethod(fake_email_exists)
Usuario.guardar = classmethod(fake_save)
Usuario.buscar_por_email = classmethod(fake_find_email)
Usuario.buscar_por_id = classmethod(fake_find_id)
client = app.test_client()

# Root and all documented form routes render.
root_response = client.get("/")
assert root_response.status_code == 200
assert "Iniciar sesión" in root_response.get_data(as_text=True)
assert client.get("/registro").status_code == 200
assert client.get("/registro").get_data(as_text=True).find('name="nombre"') < client.get("/registro").get_data(as_text=True).find('name="apellido"')

# Unauthorized access redirects and exposes a flash on the login page.
protected = client.get("/dashboard", follow_redirects=True)
assert protected.status_code == 200
assert "Debes iniciar sesión." in protected.get_data(as_text=True)
assert protected.request.path == "/"

# Invalid input cases render every validation message, never query uniqueness, and never save.
for form, expected_messages in [
    ({"nombre": "", "apellido": "", "email": "", "password": ""}, [
        "El nombre es obligatorio.", "El apellido es obligatorio.",
        "El email es obligatorio.", "La contraseña es obligatoria.",
    ]),
    ({"nombre": "J", "apellido": "P", "email": "correo", "password": "123"}, [
        "El nombre debe tener al menos 2 caracteres.",
        "El apellido debe tener al menos 2 caracteres.",
        "El email no tiene un formato válido.",
        "La contraseña debe tener al menos 8 caracteres.",
    ]),
]:
    before = len(save_calls)
    response = client.post("/registrar", data=form, follow_redirects=True)
    markup = response.get_data(as_text=True)
    assert response.request.path == "/registro"
    for message in expected_messages:
        assert message in markup
    assert len(save_calls) == before
    with client.session_transaction() as session:
        assert "password" not in session
        assert "datos_formulario" not in session

# Successful registration stores the Bcrypt hash (not the cleartext) and authenticates.
plain_password = "12345678"
registered = client.post("/registrar", data={
    "nombre": " Dany ", "apellido": " Hernández ",
    "email": " DANY@GMAIL.COM ", "password": plain_password,
}, follow_redirects=True)
registered_markup = registered.get_data(as_text=True)
assert registered.status_code == 200
assert registered.request.path == "/dashboard"
assert "Usuario creado." in registered_markup
assert "Bienvenido, Dany" in registered_markup
assert accounts["dany@gmail.com"]["password"] != plain_password
assert accounts["dany@gmail.com"]["password"].startswith("$2")
assert bcrypt.check_password_hash(accounts["dany@gmail.com"]["password"], plain_password)
assert saved_payloads[0]["password"] != plain_password
assert set(saved_payloads[0]) == {"nombre", "apellido", "email", "password"}
with client.session_transaction() as session:
    assert session.get("usuario_id") == 1
    assert plain_password not in repr(dict(session))
    assert "email" not in session

# Duplicate email is rejected before hashing/insert.
before = len(save_calls)
duplicate = client.post("/registrar", data={
    "nombre": "Dany", "apellido": "Test", "email": "DANY@gmail.com", "password": plain_password,
}, follow_redirects=True)
assert "El email ya está registrado." in duplicate.get_data(as_text=True)
assert duplicate.request.path == "/registro"
assert len(save_calls) == before

# A valid password with an unavailable DB result does not create a session.
client.get("/logout")
old_account_count = len(accounts)
original_save = Usuario.guardar
Usuario.guardar = classmethod(lambda cls, data: False)
db_error = client.post("/registrar", data={
    "nombre": "Otra", "apellido": "Cuenta", "email": "otra@example.com", "password": plain_password,
}, follow_redirects=True)
assert "No fue posible registrar el usuario." in db_error.get_data(as_text=True)
assert db_error.request.path == "/registro"
assert len(accounts) == old_account_count
with client.session_transaction() as session:
    assert "usuario_id" not in session
Usuario.guardar = original_save

# Correct login; email is normalized before lookup.
login_ok = client.post("/login", data={
    "email": " DANY@GMAIL.COM ", "password": plain_password,
}, follow_redirects=True)
assert login_ok.request.path == "/dashboard"
assert "Bienvenido, Dany" in login_ok.get_data(as_text=True)
with client.session_transaction() as session:
    assert session.get("usuario_id") == 1

# Incorrect password and nonexistent account display identical generic feedback.
wrong_password = client.post("/login", data={
    "email": "dany@gmail.com", "password": "incorrecta",
}, follow_redirects=True)
missing_user = client.post("/login", data={
    "email": "no-existe@example.com", "password": plain_password,
}, follow_redirects=True)
login_error = "Email o contraseña incorrectos."
assert login_error in wrong_password.get_data(as_text=True)
assert login_error in missing_user.get_data(as_text=True)
assert wrong_password.request.path == "/"
assert missing_user.request.path == "/"

# Dashboard reloads profile for session ID; a deleted profile invalidates session.
with client.session_transaction() as session:
    session.clear()
    session["usuario_id"] = 987
stale = client.get("/dashboard", follow_redirects=True)
assert stale.request.path == "/"
assert "Debes iniciar sesión." in stale.get_data(as_text=True)
with client.session_transaction() as session:
    assert "usuario_id" not in session

# Logout removes session and dashboard is protected again.
with client.session_transaction() as session:
    session["usuario_id"] = 1
logout = client.get("/logout")
assert logout.status_code == 302
assert logout.headers["Location"].endswith("/")
with client.session_transaction() as session:
    assert not session.get("usuario_id")
assert client.get("/dashboard").status_code == 302

print(f"Python syntax: {len(python_files)} files valid")
print("Jinja: base, login, registration, dashboard compile")
print("Validation: empty fields, short names, malformed email, short password")
print("Registration: normalized unique email, Bcrypt hash only, authenticated dashboard")
print("Duplicate and DB failure: rejected without creating a user/session")
print("Login: correct credentials succeed; wrong/unknown credentials share one message")
print("Authorization: protected dashboard redirects anonymous and stale sessions")
print("Logout: clears session; Pipenv lock verified separately")
