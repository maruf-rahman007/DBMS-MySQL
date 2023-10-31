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
                INSERT INTO Student(roll , first_name , last_name)
                VALUES(2,"Shovan","Turzo");
    
              """

mycyrsor.execute(sql_command)
mydb.commit()