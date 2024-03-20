# pip3 install mysql-connector-python
import mysql.connector

database_name = 'bank'
table_name = 'account'

db = None
cursor = None


def connect_db(username, password):
    global db
    db = mysql.connector.connect(host="localhost", user=username, password=password, database=database_name)
    print(db)


def create_cursor():
    global cursor
    cursor = db.cursor(buffered=True)


def create_database():
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")


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
    for database in cursor:
        print(database)


def insert_one_record(email, balance):
    sql_query = f"INSERT INTO {table_name} (email, balance) VALUES (%s, %s)"
    values = (email, balance)
    cursor.execute(sql_query, values)
    db.commit()  # NOTE: no records will be inserted if you don't commit
    print(f"No. of Records inserted: {cursor.rowcount}")


def insert_many(list_of_email_balance_tuples):
    # ----- SLOWER WAY -----

    # for email_balance in list_of_email_balance_tuples:
    #     insert_one_record(email_balance)

    # ----- BETTER WAY -----

    sql = f"INSERT INTO {table_name} (email, balance) VALUES (%s, %s)"
    cursor.executemany(sql, list_of_email_balance_tuples)
    db.commit()
    print(f"No. of Records inserted: {cursor.rowcount}")


def show_all_records():
    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()  # 'records' is a list of tuples
    for record in records:
        print(f"id = {record[0]} | email = {record[1]} | balance = {record[2]}")


def delete_all_records():
    cursor.execute(f"DELETE FROM {table_name}")
    db.commit()
    print(f"No. of Records deleted: {cursor.rowcount}")
