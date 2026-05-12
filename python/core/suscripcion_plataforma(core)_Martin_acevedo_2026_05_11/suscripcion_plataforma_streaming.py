class SuscripcionStreaming:
   costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

   def __init__(self, usuario, tipo_suscripcion = "Gratis"):
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

# ==========================================================
# INSTANCIAS 3 USUARIOS
# ==========================================================

# Crea 3 usuarios con diferentes tipos de suscripción
u1 = SuscripcionStreaming("Ana", "Gratis")
u2 = SuscripcionStreaming("Carlos", "Estándar")
u3 = SuscripcionStreaming("Beatriz", "Premium")

print("\n--- Pruebas Usuario 1 (Intenta ver, mejora, paga) ---")
u1.ver_contenido_exclusivo()
u1.cambiar_suscripcion("Estándar")
u1.realizar_pago(5.99)

print("\n--- Pruebas Usuario 2 (Ve, mejora, paga 2 veces) ---")
u2.ver_contenido_exclusivo()
u2.cambiar_suscripcion("Premium")
u2.realizar_pago(10.00)
u2.realizar_pago(6.98)

print("\n--- Pruebas Usuario 3 (Paga menos, ve contenido) ---")
u3.realizar_pago(5.00)
u3.ver_contenido_exclusivo()

print("\n--- Resumen Final ---")
u1.mostrar_info_suscripcion()
u2.mostrar_info_suscripcion()
u3.mostrar_info_suscripcion()


'''
 - Usa self.saldo_pendiente += self.costo_mensual para simular el cobro mensual.
 - Válida tipos de suscripción en cambiar_suscripcion para evitar errores.
 - Usa if para gestionar el acceso a contenido según la suscripción.
'''