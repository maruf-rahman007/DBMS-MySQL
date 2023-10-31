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
                CREATE TABLE Student(
                    roll INT,
                    first_name VARCHAR(20),
                    last_name VARCHAR(20)
                );
            
              """

mycyrsor.execute(sql_command)