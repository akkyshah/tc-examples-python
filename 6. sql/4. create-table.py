# pip3 install mysql-connector-python
import mysql.connector

database_name = 'bank'
table_name = 'account'


def connect_db(username, password):
    global db
    db = mysql.connector.connect(host="localhost", user=username, password=password, database=database_name)
    print(db)


def create_cursor():
    global cursor
    cursor = db.cursor(buffered=True)


def create_database(database_name):
    cursor.execute("CREATE DATABASE IF NOT EXISTS " + database_name)


def show_all_databases():
    cursor.execute("SHOW DATABASES")
    for database in cursor:
        print(database)


def create_table():
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255),
            balance INT
        )
        """
    )


def show_all_tables():
    cursor.execute("SHOW TABLES")
    for tables in cursor:
        print(tables)


connect_db('root', 'rootroot')
create_cursor()
# create_database(database_name)
# show_all_databases()
create_table()
show_all_tables()
