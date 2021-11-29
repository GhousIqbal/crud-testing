import unittest
import app
import mysql.connector

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


class Test(unittest.TestCase):
    # def test_insert(self):
    #     app.insertRow(5, 'Umer', 67579345)
    #     self.assertEqual((5, 'Umer', 67579345), app.getRow())
    #     app.printTable()

    # def test_delete(self):
    #     app.deleteRow()
    #     self.assertEqual((4, 'Malik', 47579345), app.getRow())
    #     app.printTable()

    def test_update(self):
        app.updateRow()
        self.assertEqual((4, 'Ghous', 47579345), app.getRow())
        app.printTable()


if __name__ == '__main__':
    unittest.main()
