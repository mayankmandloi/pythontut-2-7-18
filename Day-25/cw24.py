import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="mydatabase"
)

mycursor = mydb.cursor()

id=input("enter id")
name=input("enter name")
query="UPDATE `dummy` SET `name` = %s WHERE `dummy`.`id` = %s;"
val=(name,id)
print(query,val)
mycursor.execute(query,val)
mydb.commit()
#