import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

#print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE pythonTest")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)