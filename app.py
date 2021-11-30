import mysql.connector
from tabulate import tabulate

# insert MySQL Database information here
HOST = "localhost"
DATABASE = "PythonDB"
USER = "root"
PASSWORD = "admin"

# connect to the database
db_connection = mysql.connector.connect(
    host=HOST,  database=DATABASE, user=USER, password=PASSWORD)


def getServerInfo():
    # get server information
    print(db_connection.get_server_info())


# get the db cursor
cursor = db_connection.cursor()

# create database information
# cursor.execute("CREATE DATABASE PythonDB")

# cursor.execute(
#     "CREATE TABLE Customer (custID int PRIMARY KEY, Name VARCHAR(20), Contact int)")

# cursor.execute("Describe Customer")

# for x in cursor:
#     print(x)


def insertRow(ID, Name, Contact):
    cursor.execute(
        "INSERT INTO Customer (custID,Name,Contact) VALUES (%s,%s,%s)", (ID, Name, Contact))
    db_connection.commit()


def deleteRow():
    cursor.execute("DELETE from Customer where custID=5")
    db_connection.commit()


def updateRow():
    cursor.execute("UPDATE Customer set Name = 'Ghous' where Name = 'Malik'")
    db_connection.commit()


def getRow():

    cursor.execute("SELECT * from Customer ORDER BY custID DESC LIMIT 1")
    # get all selected rows
    row = cursor.fetchall()
    # print all rows in a tabular format
    return row[0]

    # for x in cursor:
    #     print(x)


def printTable():
    cursor.execute("SELECT * from Customer")
    # get all selected rows
    rows = cursor.fetchall()
    # print all rows in a tabular format
    print(tabulate(rows, headers=cursor.column_names))
    for x in cursor:
        print(x)


printTable()
print(getRow())
