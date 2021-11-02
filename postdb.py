from sort import *
import mysql.connector

def connector(host,user,password):

    try:
        mydb = mysql.connector.connect(
            host = host,
            user = user,
            passwd = password
        )
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        for database in mycursor:
            if database[0] == "exercicepython":
                
        # data = sort()
        # print(data)
    except mysql.connector.errors.ProgrammingError:
        print("One of your keys is not correct please fix it")
        

    

connector("localhost","root","")