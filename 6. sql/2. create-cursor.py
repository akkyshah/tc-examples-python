# pip3 install mysql-connector-python
import mysql.connector

db = None
cursor = None


def connect_db(username, password):
    global db
    db = mysql.connector.connect(host="localhost", user=username, password=password)
    print(db)


def create_cursor():
    global cursor
    cursor = db.cursor(buffered=True)


connect_db('root', 'rootroot')
create_cursor()

