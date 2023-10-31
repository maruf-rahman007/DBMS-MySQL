import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Maruf007-",
    database = "mydatabase"
)

# Create a Database
mycyrsor = mydb.cursor()

sql_command = """
                UPDATE Student
                SET first_name = "Sarbajit"
                WHERE roll = 2;
    
              """

mycyrsor.execute(sql_command)
mydb.commit()