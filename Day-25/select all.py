import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="cns"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM `user`"
mycursor.execute(sql)
myresult=mycursor.fetchall()

for x in myresult:
    print("Name:-",x[5])
