import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Dani",
  password="pass123",
  database="mydata"
  
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydata")
mycursor.execute("CREATE TABLE customers (name VARCHAR(200) , address VARCHAR(200))")
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


