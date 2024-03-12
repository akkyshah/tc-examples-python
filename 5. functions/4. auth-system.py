database = [
    (1, "john@example.com", "Pass123"),
    (2, "peter@example.com", "Pass456"),
    (3, "eric@example.com", "Pass789")
]


def login(email, password):
    result = False
    for record in database:
        if record[1] == email and record[2] == password:
            result = True
            break
    return result


def attempt_login():
    login_attempt_count = 0
    for i in range(0, 3):
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        result = login(email, password)
        if result == True:
            break
        else:
            login_attempt_count += 1
            print("login failed")

    if login_attempt_count == 3:
        print("Try again after 1 hour.")
    else:
        print("login Successful")


def register():
    email = input("\nEnter an Email: ")
    pwd = input("Enter your password: ")

    found = False
    for record in database:
        if record[1] == email:
            found = True
            break

    if found:
        print("Email already exist. Cant register with duplicate email.")
    else:
        last_record = database[-1]  # (3, "eric@example.com", "Pass789")
        last_record_id = last_record[0]
        next_record_id = last_record_id + 1
        new_record = (next_record_id, email, pwd)
        database.append(new_record)
        print(f"Created email: {email}")

def print_all_records():
    print("\nprinting all emails: ")
    for record in database:
        print(record[1])


def run():
    n = input("Enter your option:")
    while n != '0':
        match n:
            case "1":
                register()
            case "2":
                attempt_login()
            case "3":
                print_all_records()
            case _:
                print("Invalid option. Try again")
        n = input("\nEnter your option:")


run()
