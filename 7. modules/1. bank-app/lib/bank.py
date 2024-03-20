import sql


def deposit_money(email, amount):
    sql_query = f"UPDATE {sql.table_name} SET balance = balance + %s WHERE email = %s"
    values = (amount, email)
    sql.cursor.execute(sql_query, values)
    sql.db.commit()  # NOTE: no records will be inserted if you don't commit
    print(f"No. of Records updated: {sql.cursor.rowcount}")


def withdraw_money(email, amount):
    sql_query = f"UPDATE {sql.table_name} SET balance = balance - %s WHERE email = %s"
    values = (amount, email)
    sql.cursor.execute(sql_query, values)
    sql.db.commit()  # NOTE: no records will be inserted if you don't commit
    print(f"No. of Records updated: {sql.cursor.rowcount}")


def show_single_record(email):
    sql.cursor.execute(f"SELECT * FROM {sql.table_name} WHERE email = '{email}'")
    record = sql.cursor.fetchone()  # 'record' is a single-tuple OR None
    print(f"id = {record[0]} | email = {record[1]} | balance = {record[2]}")
