

'''
Escenario 2 — Sistema de Gimnasio
Un gimnasio necesita un sistema para administrar sus clientes, entrenadores y planes de entrenamiento.
El sistema permitirá organizar la información de los usuarios y sus actividades.
Clases sugeridas
Cliente

Entrenador

PlanEntrenamiento

Métodos sugeridos

Clase Cliente

mostrar_cliente()

actualizar_telefono()

Clase Entrenador

mostrar_entrenador()

asignar_cliente()

Clase PlanEntrenamiento

mostrar_plan()

modificar_duracion()

'''

class PlanEntrenamiento:

    def __init__(self, nombre_plan, duracion_plan):

        self.nombre_plan = nombre_plan

        self.duracion_plan = duracion_plan

    def mostrar_plan(self):

        print(f"{self.nombre_plan} | {self.duracion_plan}")

    def modificar_duracion(self):

        cambio = input("A cuanto tiempo quieres cambiar la duración?\n")

        self.duracion_plan = cambio

       

        print(f"El plan de {self.nombre_plan} cambio su tiempo a {cambio} Semanas")

plan1 = PlanEntrenamiento("Fuerza", "4 Semanas")

plan2 = PlanEntrenamiento("Pilometria", "2 Semanas")

plan3 = PlanEntrenamiento("Pierna", "2 Semanas")


class Cliente:

    def __init__(self,nombre, numero, correo):

        self.nombre = nombre

        self.numero = numero

        self.correo = correo

    def mostrar_cliente(self):

        print(f"Nombre: {self.nombre} Número: {self.numero} Correo: {self.correo}")


    def actualizar_telefono(self):

        numero_antiguo = self.numero

        cambiar_num = input("Realiza el cambio de número\n")

        self.numero = cambiar_num

        print(f"El numero {numero_antiguo} cambió a {cambiar_num}\n")

cliente1 = Cliente("José", "932494323", "José@gmail.com")

cliente2 = Cliente("Martina", "932674532", "Martina@gmail.com")

cliente3 = Cliente("Luciano", "932895643", "Luciano@gmail.com")


class Entrenador:

    def __init__(self, nombre_entrenador, numero_entrenador, correo_entrenador):

        self.nombre_entrenador = nombre_entrenador

        self.numero_entrenador = numero_entrenador

        self.correo_entrenador = correo_entrenador

       

    def mostrar_entrenador(self):

        print(f"Nombre: {self.nombre_entrenador} Número: {self.numero_entrenador} Correo: {self.correo_entrenador}")

       

    def asignar_cliente(self, cliente_objeto):

        print(f"{cliente_objeto.nombre} se ha asignado a {self.nombre_entrenador}")



   



entrenador1 = Entrenador("Marcos", "932293363", "Marcos@gmail.com")

entrenador2 = Entrenador("Sofia", "921296383", "sofia@gmail.com")

entrenador3 = Entrenador("Luis", "932192346", "luis@gmail.com")



continuar = True



while continuar:

    opcion = input("\n---- Elige una opción: (1-6) (0 para salir) =")

    if opcion == "1":

        print("\nEjecutando ejercicio 1:")

        plan1.mostrar_plan()

        plan2.mostrar_plan()

        plan3.mostrar_plan()

    elif opcion == "2":

        print("\nEjecutando ejercicio 2:")

        print("1\n2\n3")

        plan = input("Ingrese a cual quiere cambiar\n")

        if plan == "1":

            plan1.modificar_duracion()

        elif plan == "2":

            plan2.modificar_duracion()

        elif plan == "3":

            plan3.modificar_duracion()

        else:

            print("Ingrese una opción Valida.")

    elif opcion == "3":

        print("\nEjecutando ejercicio 3")

        cliente1.mostrar_cliente()

        cliente2.mostrar_cliente()

        cliente3.mostrar_cliente()

    elif opcion == "4":

        print("1\n2\n3")

        plan = input("Ingrese a cual cliente quiere cambiar su número\n")

        if plan == "1":

            cliente1.actualizar_telefono()

        elif plan == "2":

            cliente2.actualizar_telefono()

        elif plan == "3":

            cliente3.actualizar_telefono()

        else:

            print("Ingrese una opción Valida.")

    elif opcion == "5":

        entrenador1.mostrar_entrenador()

        entrenador2.mostrar_entrenador()

        entrenador3.mostrar_entrenador()

    elif opcion == "6":

        print("1\n2\n3")

        plan = input("Ingrese a cual entrenador quiere elegir\n")

        if plan == "1":

            entrenador1.asignar_cliente(cliente1)

        elif plan == "2":

            entrenador2.asignar_cliente(cliente3)

        elif plan == "3":

            entrenador3.asignar_cliente(cliente2)

        else:

            print("Ingrese una opción Valida.")

    elif opcion == "0":

        print("Saliendo...")

        continuar = False

    else:

        print("Opción no válida, intente otra vez")