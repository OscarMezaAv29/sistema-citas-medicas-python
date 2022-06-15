import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "oama_citas_python",
        port = 3306
    )

    #print(database)

    cursor = database.cursor(buffered = True)

    return [database, cursor]
