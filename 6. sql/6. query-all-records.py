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


def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS " + database_name)


def show_all_databases():
    cursor.execute("SHOW DATABASES")
    for database in cursor:
        print(database)


def create_table():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS {} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255),
            balance INT
        )
        """.format(table_name)
    )


def show_all_tables():
    cursor.execute("SHOW TABLES")
    for table in cursor:
        print(table)


def insert_one_record(email, balance):
    sql_query = "INSERT INTO {} (email, balance) VALUES (?, ?)".format(table_name)
    values = (email, balance)
    cursor.execute(sql_query, values)
    db.commit()  # NOTE: no records will be inserted if you don't commit
    print(f"No. of Records inserted: {cursor.rowcount}")


def show_all_records():
    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()  # 'records' is a list of tuples
    for record in records:
        print(record)
        # ------ Also Try Following ------
        # print(f"id = {record[0]} | email = {record[1]} | balance = {record[2]}")


connect_db('root', 'rootroot')
create_cursor()
# create_database()
# show_all_databases()
# create_table()
# show_all_tables()
# insert_one_record('john@example.com', 100)
show_all_records()
