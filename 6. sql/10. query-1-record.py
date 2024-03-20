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
    cursor.execute("CREATE DATABASE IF NOT EXISTS bank")


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
    for table in cursor:
        print(table)


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


def show_single_record(email):
    sql_query = f"SELECT * FROM {table_name} WHERE email = '{email}'"
    cursor.execute(sql_query)
    record = cursor.fetchone()  # 'record' is a single-tuple OR None
    if record is not None:
        print(f"id = {record[0]} | email = {record[1]} | balance = {record[2]}")
    else:
        print('record not found')


def delete_all_records():
    cursor.execute(f"DELETE FROM {table_name}")
    db.commit()
    print(f"No. of Records deleted: {cursor.rowcount}")


def deposit_money(email, amount):
    sql = f"UPDATE {table_name} SET balance = balance + %s WHERE email = %s"
    values = (amount, email)
    cursor.execute(sql, values)
    db.commit()  # NOTE: no records will be inserted if you don't commit
    print(f"No. of Records updated: {cursor.rowcount}")


def withdraw_money(email, amount):
    sql = f"UPDATE {table_name} SET balance = balance - %s WHERE email = %s"
    values = (amount, email)
    cursor.execute(sql, values)
    db.commit()  # NOTE: no records will be inserted if you don't commit
    print(f"No. of Records updated: {cursor.rowcount}")


connect_db('root', 'rootroot')
create_cursor()
# create_database()
# show_all_databases()
# create_table(table_name)
# show_all_tables()
# insert_one_record(table_name, 'john@example.com', 100)
"""
insert_many([
    ('tyler@example.com', 2000),
    ('peter@example.com', 5000),
    ('eric@example.com', 10000),
    ('mike@example.com', 15000),
])
"""

# show_all_records()

# deposit_money("mike@example.com", 5000)
# withdraw_money("mike@example.com", 10000)

show_single_record("mike@example.com")

delete_all_records()
