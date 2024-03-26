import auth
import bank
import sql


def configure():
    sql.connect_db('root', 'rootroot')
    sql.create_cursor()
    auth.init()
    bank.init()


def run():
    configure()

    msg = '\n1. Login\n2. Register\n0. Quit\n'
    print(msg)
    option = input('\tEnter you option:')
    while option != '0':
        match option:
            case '1':
                result, email = auth.login()
                if result is True:
                    bank.run(email)
            case '2':
                auth.register()
            case _:
                print('\n\t\tinvalid option')

        print(msg)
        option = input('Enter you option:')

    print('Thank you for using our services.')


run()
