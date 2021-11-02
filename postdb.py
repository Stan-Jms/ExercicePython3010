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
                return database[0]
        return False
    except mysql.connector.errors.ProgrammingError:
        print("One of your keys is not correct please fix it")
        return False
        

def send(host,user,password):
    value = connector(host,user,password)
    data = sort()
    if value != False:
        mydb = mysql.connector.connect(
            host = host,
            user = user,
            passwd = password,
            database = value
        )
        print(data)
            #sendObject(mydb,)

        



def sendObject(db,tuple,type):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM jsp")
    res = mycursor.fetchall()
    print(res)
    
send("localhost","root","")