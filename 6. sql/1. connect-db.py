# pip3 install mysql-connector-python
import mysql.connector

db = None

def connect_db(username, password):
    global db
    db = mysql.connector.connect(host="localhost", user=username, password=password)
    print(db)


connect_db('root', 'rootroot')
