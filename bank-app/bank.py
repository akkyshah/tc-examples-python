import matplotlib.pyplot as plt

import fileio
import sql

accounts = "accounts"
transactions = "transactions"


def init():
    sql.execute_query(
        """
        CREATE TABLE IF NOT EXISTS {} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255),
            balance DECIMAL
        )
        """.format(accounts)
    )
    sql.execute_query(
        """
        CREATE TABLE IF NOT EXISTS {} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255),
            date DATE,
            message VARCHAR(255),
            amount DECIMAL
        )
        """.format(transactions)
    )


def create_customer(email):
    sql_query = "INSERT INTO {} (email, balance) VALUES (%s, %s)".format(accounts)
    sql.update_or_insert(sql_query, (email, 0))


def find_customer_by_email(email):
    return sql.fetch_one("SELECT * FROM {} WHERE email = '{}'".format(accounts, email))


def deposit_money(email, amount, date):
    update_balance_sql_query = "UPDATE {} SET balance = balance + %s WHERE email = %s".format(accounts)
    values = (amount, email)
    sql.update_or_insert(update_balance_sql_query, values)

    insert_transaction_query = "INSERT INTO {} (email, date, message, amount) VALUES (%s, %s, %s, %s)".format(
        transactions)
    values = (email, date, "Deposited", amount)
    sql.update_or_insert(insert_transaction_query, values)
    print(f"\t\tDeposit money successful")
    return True


def withdraw_money(email, amount, date):
    balance = get_balance(email)
    if balance < amount:
        print(f"\t\tCannot Withdraw - Low balance")
        return False

    update_balance_sql_query = "UPDATE {} SET balance = balance - %s WHERE email = %s".format(accounts)
    values = (amount, email)
    sql.update_or_insert(update_balance_sql_query, values)

    insert_transaction_query = "INSERT INTO {} (email, date, message, amount) VALUES (%s, %s, %s, %s)".format(
        transactions)
    values = (email, date, "Withdrawn", amount)
    sql.update_or_insert(insert_transaction_query, values)
    print(f"\t\tWithdraw money successful")
    return True


def get_balance(email):
    record = find_customer_by_email(email)
    if record is None:
        return 0
    balance = record[2]
    return balance


def get_transactions(email):
    return sql.fetch_all("SELECT * FROM {} WHERE email = '{}' ORDER BY date DESC".format(transactions, email))


def show_transactions(email):
    records = get_transactions(email)
    if len(records) == 0:
        print("No transactions done so far.")
        return
    for record in records:
        print(f'\t{record[2]} - {record[3]} - ${record[4]}')


def export_transactions(email):
    records = get_transactions(email)
    fileio.save_csv('transactions.csv', ('ID', 'email', 'date', 'message', 'amount'), records)


def account_balance_chart(email):
    records = get_transactions(email)
    records.reverse()

    dates = [record[2] for record in records]

    eod_balances = []
    count = 0
    for record in records:
        balance = record[4]
        if record[3] == "Deposited":
            count += balance
        else:
            count -= balance
        eod_balances.append(count)

    fig, ax = plt.subplots()
    ax.plot(dates, eod_balances)
    ax.set_ylabel('Amount')
    ax.set_title('Balance Chart')
    plt.show()


def run(email):
    msg = '\nLogged In User: {}\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Show Transactions\n5. Export Transactions\n6. Show Account Balance Chart\n0. Logout\n'.format(
        email)
    print(msg)
    option = input('\n\tEnter you option:')
    while option != '0':
        match option:
            case '1':
                amount = float(input('\n\tEnter an Amount to Deposit:'))
                date = input('\tEnter Date (yyyy-mm-dd) :')
                deposit_money(email, amount, date)
            case '2':
                amount = float(input('\n\tEnter an Amount to Withdraw:'))
                date = input('\tEnter Date (yyyy-mm-dd) :')
                withdraw_money(email, amount, date)
            case '3':
                print(f'\n\tCurrent Balance: {get_balance(email)}')
            case '4':
                show_transactions(email)
            case '5':
                export_transactions(email)
                print(f'\n\tExport Successful')
            case '6':
                account_balance_chart(email)
            case _:
                print('\n\t\tinvalid option')

        print(msg)
        option = input('Enter you option:')
    print('\n\tLogging Out...')
