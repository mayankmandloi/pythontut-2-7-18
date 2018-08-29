import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="webbhumi"
)

mycursor = mydb.cursor()

select=input("enter 'r' to read 'c' to create 'u' to update 'd' to delete")
if select == 'r':
    sql = "SELECT * FROM `dummy`"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print("Name:-", x[1])
else:
    if select == 'c':
        id = input("enter id")
        name = input("enter name")
        number = input("enter number")
        password = input("enter password")
        sql = "insert into `dummy` (`id`, `name`, `number`, `password`) values (%s ,%s ,%s ,%s);"
        val = (id, name, number, password)
        mycursor.execute(sql, val)
        mydb.commit()

    else:
        if select == 'u':
            id = input("enter id to update")
            password = input("enter new password")
            """ 
            sql = "UPDATE `dummy` SET `password` = %s WHERE `dummy`.`id` = %s;"
            val = (password, id)
            mycursor.execute(sql, val)
            """    """ 
            sql = "UPDATE `dummy` SET `password` = %s WHERE `dummy`.`id` = %s;"
            val = (password, id)
            mycursor.execute(sql, val)
            """

            sql = "UPDATE `dummy` SET `password` = '"+password+"' WHERE `dummy`.`id` = "+id+";"
            mycursor.execute(sql)
            mydb.commit()
        else:
            if select == 'd':
                id=input("Enter id to delete")
                sql ="DELETE FROM `dummy` WHERE `id` = "+id+";"
                mycursor.execute(sql)
                mydb.commit()
            else:
                print("Wrong choice")