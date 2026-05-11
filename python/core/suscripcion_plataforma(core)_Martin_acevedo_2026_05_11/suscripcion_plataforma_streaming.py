class SuscripcionStreaming:
   costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

   def __init__(self, usuario, saldo_pendiente, tipo_suscripcion = "Gratis"):
       self.usuario = usuario
       self.tipo_suscripcion = tipo_suscripcion
       self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
       self.saldo_pendiente = self.costo_mensual #Se simula el primer pago


def realizar_pago(self, monto):
        self.saldo_pendiente -= monto
        print(f"Pagaste {monto}. Saldo pendiente: {self.saldo_pendiente}")

def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
            # Sumamos el nuevo costo al saldo según tus instrucciones
            self.saldo_pendiente += self.costo_mensual
            print(f"Cambiado a {nuevo_tipo}")
        else:
            print("Tipo de suscripción no válido")

def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Gratis":
            print("No tienes acceso a contenido exclusivo.")
        else:
            print(f"Disfrutando contenido exclusivo como usuario {self.tipo_suscripcion}.")

def mostrar_info_suscripcion(self):
        print(f"Usuario: {self.usuario} | Plan: {self.tipo_suscripcion} | Saldo: {self.saldo_pendiente}")



'''
 - Usa self.saldo_pendiente += self.costo_mensual para simular el cobro mensual.
 - Válida tipos de suscripción en cambiar_suscripcion para evitar errores.
 - Usa if para gestionar el acceso a contenido según la suscripción.
'''