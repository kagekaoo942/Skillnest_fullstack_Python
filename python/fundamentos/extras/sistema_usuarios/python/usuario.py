from python.fundamentos.extras.sistema_usuarios.python.conexion import conexion, cursor

class usuario:
    def _init_(self, username, password, admin=False):
        self.username = username
        self.password = password
        self.admin = admin

#Creacion usuario normal
usuario_normal = usuario("Carlos")

#Creacion de usuario admin
usuario_admin = usuario("Ana", admin=True)