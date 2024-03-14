# pip3 install mysql-connector-python
import mysql.connector

database_name = 'bank'


def connect_db(username, password):
    global db
    db = mysql.connector.connect(host="localhost", user=username, password=password)
    print(db)


def create_cursor():
    global cursor
    cursor = db.cursor(buffered=True)


def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS " + database_name)


def show_all_databases():
    cursor.execute("SHOW DATABASES")
    for database in cursor:
        print(database)


connect_db('root', 'rootroot')
create_cursor()
create_database()
show_all_databases()
