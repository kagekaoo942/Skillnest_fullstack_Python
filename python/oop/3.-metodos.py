class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0

   def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
       self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido


def aumentarCredito(self, aumento):
    self.limite_credito += aumento
def cambiarCorreo(self,email):
    self.email = email

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

#Instancias de la clase
miyagi.hacer_compra(2000)
print(f"Primera compra de: {miyagi.nombre}: ${miyagi.saldo}")
print()
miyagi.hacer_compra(300)
print(f"Segunda compra: {miyagi.saldo_pagar}")
#Imprimir cuanto credito le queda a miyagi
print(f"Credito disponible: {miyagi.limite_credito - miyagi.saldo_pagar}")
daniel.hacer_compra(45)

#Compras de daniel 2 compras y muestra saldo a pagar
print("---------compras de daniel------------")
print(daniel.saldo_pagar) #Imprime: 45

'''
1.-Crear un nuevo método que permita aumentar el límite de crédito.
Imprimir el nuevo límite de crédito


2.-Crear un método que permita cambiar el correo de la instancia..
Mostrar el nuevo correo.
'''
#1.
miyagi.aumentarCredito(2000)
print(f"El nuevo limite de credito es: {miyagi.limite_credito}")

#2.
miyagi.cambiarCorreo("miyagi@gmail.com")
print(f"El nuevo correo establecido es: {miyagi.email}")
