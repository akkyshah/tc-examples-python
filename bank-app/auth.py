import bank
import sql

users = 'users'


def init():
    sql.execute_query(
        """
        CREATE TABLE IF NOT EXISTS {} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255),
            password VARCHAR(255)
        )
        """.format(users)
    )


def find_one_user(email, password):
    return sql.fetch_one("SELECT * FROM {} WHERE email = '{}' AND password = '{}'".format(users, email, password))


def insert_one_user(email, password):
    sql_query = "INSERT INTO {} (email, password) VALUES (%s, %s)".format(users)
    sql.update_or_insert(sql_query, (email, password))
    bank.create_customer(email)
    print(f"Registered Successfully")


def login():
    for i in range(0, 3):
        print(f'\n\tAttempt {i + 1}')
        email = input('\t\tEmail:')
        password = input('\t\tPassword:')

        record = find_one_user(email, password)

        if record is None:
            print('invalid email/password combination')
        else:
            return True, email
    print('\n\tYou have used all 3 attempts, please try again later')
    return False, None


def register():
    email = input('\n\tEmail:')
    password = input('\tPassword:')
    insert_one_user(email, password)
    return True
