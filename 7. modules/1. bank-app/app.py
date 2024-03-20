from lib import bank, sql


def configure_sql():
    sql.connect_db('root', 'rootroot')
    sql.create_cursor()
    # sql.create_database()
    # sql.show_all_databases()
    # sql.create_table(table_name)
    # sql.show_all_tables()


def insert_dummy_data():
    # sql.insert_one_record(table_name, 'john@example.com', 100)
    sql.insert_many([
        ('tyler@example.com', 2000),
        ('peter@example.com', 5000),
        ('eric@example.com', 10000),
        ('mike@example.com', 15000),
    ])
    sql.show_all_records()


def clear_data():
    sql.delete_all_records()


def run():
    configure_sql()
    insert_dummy_data()
    bank.deposit_money("mike@example.com", 5000)
    bank.withdraw_money("mike@example.com", 10000)
    bank.show_single_record("mike@example.com")
    clear_data()


run()
