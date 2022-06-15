import doctores.doctor as modelo
import citas.acciones


class Acciones:

    def registro(self):
        print("Se procederá a realizar tu registro en el sistema...")

        nombre = input("Introduzca su nombre: ")
        apellidos = input("Introduzca sus apellidos: ")
        cedula = input("Introduzca su cédula: ")
        especialidad = input("Introduzca su especialidad: ")
        consultorio = input("Introduzca su consultorio: ")
        email = input("Introduzca su email: ")
        password = input("Introduzca su contraseña: ")

        doctor = modelo.Doctor(nombre, apellidos, cedula, especialidad, consultorio, email, password)
        registro = doctor.registrar()

        if registro[0] >= 1:
            print(f"\nBienvenido {registro[1].nombre} se ha registrado con el email {registro[1].email}")
        else:
            print("Lo siento, no se ha podido registrar. Intente nuevamente. ")

    def login(self):
        try:
            email = input("Ingrese su email: ")
            password = input("Ingrese su contraseña: ")

            doctor = modelo.Doctor('', '', '', '', '', email, password)
            login = doctor.identificar()

            if email == login[6]:
                print(f"\nBienvenido {login[1]}, se registró en el sistema el {login[8]}")
                self.proximasAcciones(login)

        except Exception as e:

            print("\nLogin incorrecto!! Inténtelo más tarde.")

    def proximasAcciones(self, doctor):
        print("""
            - Crear cita (crear)
            - Mostrar citas (mostrar)
            - Eliminar cita (eliminar)
            - Salir (salir)
        """)

        accion = input("¿Qué quieres hacer?: ")
        hazEl = citas.acciones.Acciones()

        if accion == "crear":
            print("Crear una cita")
            hazEl.crear(doctor)
            self.proximasAcciones(doctor)
        
        elif accion == "mostrar":
            hazEl.mostrar(doctor)
            self.proximasAcciones(doctor)

        elif accion == "eliminar":
            hazEl.borrar(doctor)
            self.proximasAcciones(doctor)

        elif accion == "salir":
            exit()
    