import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Maruf007-",
    database = "hr"
)

# Create a Database
mycyrsor = mydb.cursor()

sql_command = """
                SELECT * 
                FROM employees
                WHERE salary > 100
                LIMIT 10;
              """

mycyrsor.execute(sql_command)
data = mycyrsor.fetchall()

for i in data :
    print(i)