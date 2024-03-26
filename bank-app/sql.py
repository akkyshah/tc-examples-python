# pip3 install mysql-connector-python
import mysql.connector

database_name = 'bank'

db = None
cursor = None


def connect_db(username, password):
    global db
    db = mysql.connector.connect(host="localhost", user=username, password=password, database=database_name)
    print(db)


def create_cursor():
    global cursor
    cursor = db.cursor(buffered=True)


def execute_query(sql_query):
    cursor.execute(sql_query)


def update_or_insert(sql_query, values):
    cursor.execute(sql_query, values)
    db.commit()  # NOTE: no records will be inserted if you don't commit
    return cursor.rowcount


def fetch_all(sql_query):
    execute_query(sql_query)
    records = cursor.fetchall()  # 'records' is a list of tuples
    return records


def fetch_one(sql_query):
    execute_query(sql_query)
    records = cursor.fetchone()  # 'record' is a tuples | None
    return records
