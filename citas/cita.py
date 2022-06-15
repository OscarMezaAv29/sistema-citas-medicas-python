import doctores.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Cita:
    def __init__(self, doctor_id, nombre_paciente="", telefono="", descripcion=""):
        self.doctor_id = doctor_id
        self.nombre_paciente = nombre_paciente
        self.telefono = telefono
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO citas VALUES(null, %s, %s, %s, %s, NOW())"
        cita = (self.doctor_id, self.nombre_paciente, self.telefono, self.descripcion)

        cursor.execute(sql, cita)
        database.commit()

        return [cursor.rowcount, self]

    def listar(self):
        sql = f"SELECT * FROM citas WHERE doctor_id = {self.doctor_id}"
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
        
    def eliminar(self):
        sql = f"DELETE FROM citas WHERE doctor_id = {self.doctor_id} AND nombre_paciente LIKE '%{self.nombre_paciente}%'"

        cursor.execute(sql)
        database.commit()

        return[cursor.rowcount, self]

