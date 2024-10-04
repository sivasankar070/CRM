import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Sivasankar#7',
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATaBASE siva")