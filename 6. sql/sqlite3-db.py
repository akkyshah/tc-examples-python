import sqlite3


def connect_db(database):
    global db
    db = sqlite3.connect(database + ".db")
    print(db)


def create_cursor():
    global cursor
    cursor = db.cursor()


# def create_database():
#     cursor.execute("CREATE DATABASE IF NOT EXISTS bank")
#
#
# def show_all_databases():
#     cursor.execute("SHOW DATABASES")
#     for database in cursor:
#         print(database)


def create_table():
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            email VARCHAR(255),
            balance INTEGER
        )
        """
    )


def show_all_tables():
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table'")
    for table in cursor:
        print(table)


def insert_one_record(email, balance):
    sql_query = f"INSERT INTO {table_name} (email, balance) VALUES (?, ?)"
    values = (email, balance)
    cursor.execute(sql_query, values)
    db.commit()  # NOTE: no records will be inserted if you don't commit
    print(f"No. of Records inserted: {cursor.rowcount}")


def insert_many(list_of_email_balance_tuples):
    sql = f"INSERT INTO {table_name} (email, balance) VALUES (?, ?)"
    cursor.executemany(sql, list_of_email_balance_tuples)
    db.commit()
    print(f"No. of Records inserted: {cursor.rowcount}")


def show_all_records():
    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()  # 'records' is a list of tuples
    for record in records:
        print(f"id = {record[0]} | email = {record[1]} | balance = {record[2]}")


def show_single_record(email):
    cursor.execute(f"SELECT * FROM {table_name} WHERE email = '{email}'")
    record = cursor.fetchone()  # 'record' is a single-tuple OR None
    print(f"id = {record[0]} | email = {record[1]} | balance = {record[2]}")


def delete_all_records():
    cursor.execute(f"DELETE FROM {table_name}")
    db.commit()
    print(f"No. of Records deleted: {cursor.rowcount}")


def deposit_money(email, amount):
    sql = f"UPDATE {table_name} SET balance = balance + ? WHERE email = ?"
    values = (amount, email)
    cursor.execute(sql, values)
    db.commit()  # NOTE: no records will be inserted if you don't commit
    print(f"No. of Records updated: {cursor.rowcount}")


def withdraw_money(email, amount):
    sql = f"UPDATE {table_name} SET balance = balance - ? WHERE email = ?"
    values = (amount, email)
    cursor.execute(sql, values)
    db.commit()  # NOTE: no records will be inserted if you don't commit
    print(f"No. of Records updated: {cursor.rowcount}")


database_name = 'bank'
table_name = 'account'

connect_db(database_name)
create_cursor()
# create_database()
# show_all_databases()
create_table()
show_all_tables()
# insert_one_record(table_name, 'john@example.com', 100)

insert_many([
    ('tyler@example.com', 2000),
    ('peter@example.com', 5000),
    ('eric@example.com', 10000),
    ('mike@example.com', 15000),
])

deposit_money("mike@example.com", 5000)  # Mike's new balance at this point: 20000
withdraw_money("mike@example.com", 10000)  # Mike's new balance after this: 10000
show_single_record("mike@example.com")

show_all_records()

delete_all_records()
