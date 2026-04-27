#Creacio de la clase usuario - Entidad 
class Usuario:
   def _init_(self): #Constructor
             self.nombre = "Nariyoshi"
             self.apellido = "Miyagi"
             self.email = "miyagi@codingdojo.la"
             self.limite_credito = 30000
             self.saldo_pagar = 0
#Instancias de una clase
miyagi =Usuario()
daniel = Usuario()
dany = Usuario()

print(dany.nombre)

#Valores a nueva instancia
dany.nombre = "Dany"
dany.apellido = "Hernandez"
dany.email = "dany@gmail.com"
dany.limite_credito = 1000
dany.saldo_pagar = 20000

#Imprimir nombre de cada de instancia
print(miyagi.nombre)
print(daniel.nombre)
print(dany.nombre)

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido) #Imprime: Miyagi
print(miyagi.email) #Imprime: miyagi@codingdojo.la
print(miyagi.limite_credito) #Imprime:30000 
print(miyagi.saldo_pagar) #Imprime: 0

#Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
miyagi.email = "daniel@gmail.com" #Imprime: miyagi@codingdojo.la
miyagi.limite_credito = 100000 #Imprime:30000 
miyagi.saldo_pagar = 300000 #Imprime: 0
