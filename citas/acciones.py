import citas.cita as modelo

class Acciones:

    def crear(self, doctor):
        print(f"Hola {doctor[1]}! Cree una nueva cita.")

        nombre_paciente = input("Introduzca el nombre del paciente: ")
        telefono = input("Introduzca el telefono de tu paciente: ")
        descripcion = input("Introduzca una descripción de la cita: ")

        cita = modelo.Cita(doctor[0], nombre_paciente, telefono, descripcion)
        guardar = cita.guardar()

        if guardar[0] >= 1 :
            print(f"\nPerfecto! Se ha agendado la cita para el paciente: {cita.nombre_paciente}")
        else:
            print(f"\nNo se podido agendar la cita, intèntalo más tarde: {doctor[1]}")

    def mostrar(self, doctor_id):
        print(f"\n{doctor_id[1]} Estas son tus citas")

        cita = modelo.Cita(doctor_id[0])
        citas = cita.listar()

        for cita in citas:
            print("\n*****************")
            print("Nombre del paciente: ")
            print(cita[2])
            print("\nTeléfono del paciente: ")
            print(cita[3])
            print("\nDetalles de la cita: ")
            print(cita[4])
            print("\nFecha de la cita: ")
            print(cita[5])
            print("*****************\n")

    def borrar(self, doctor):
        print(f"\n{doctor[1]}!!! Borra tus citas")

        nombre_paciente = input("\nIntroduce nombre del paciente: ")
        cita = modelo.Cita(doctor[0], nombre_paciente)
        eliminar = cita.eliminar()

        if eliminar[0] >= 1:
            print(f"\nSe borró la cita del paciente: {cita.nombre_paciente}")
        else:
            print("\nNo se borró la cita, prueba mas tarde...")