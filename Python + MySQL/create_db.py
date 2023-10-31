import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Maruf007-",
)

# Create a Database
mycyrsor = mydb.cursor()

db_name = "mydatabase"
sql_command = "CREATE DATABASE "+db_name

mycyrsor.execute(sql_command)
