import datetime
import hashlib
import doctores.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Doctor:

    def __init__(self, nombre, apellidos, cedula, consultorio, especialidad, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula
        self.consultorio = consultorio
        self.especialidad = especialidad
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO doctores VALUES(null, %s, %s, %s, %s, %s, %s, %s, %s)"
        doctor = (self.nombre, self.apellidos, self.cedula, self.consultorio, self.especialidad, self.email, cifrado.hexdigest(), fecha)


        try:
            cursor.execute(sql, doctor)
            database.commit()
            return [cursor.rowcount, self]
        except:
            result = [0,self]
        return result

    def identificar(self):
        sql = "SELECT * FROM doctores WHERE email = %s AND password = %s"

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        doctor = (self.email, cifrado.hexdigest())

        cursor.execute(sql, doctor)
        result = cursor.fetchone()

        return result