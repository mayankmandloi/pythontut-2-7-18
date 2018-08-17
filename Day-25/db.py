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
number=input("enter number")
password=input("enter password")
query="insert into `dummy` (`id`, `name`, `number`, `password`) values (%s ,%s ,%s ,%s);"
val=(id,name,number,password)
mycursor.execute(query,val)
mydb.commit()

"UPDATE `dummy` SET `name` = 'south' WHERE `dummy`.`id` = 1"

