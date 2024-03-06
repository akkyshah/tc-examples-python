print("\n === Welcome to our Bank === \n")

balance = 0
transactions = []

msg = "\n1. Deposit \n2. Withdraw \n3. Check balance \n4. Show Transactions \n0. Quit\n"
print(msg)
str = input("Enter your option: ")

while str != "0":

    match str:
        case "1":
            num = int(input("\tEnter amount: "))
            balance += num
            print(f"\t\t> Deposited: ${num}")
            transactions.insert(0, f"Deposited: ${num}")

        case "2":
            num = int(input("\tEnter amount: "))
            if num <= balance:
                balance -= num
                print(f"\t\t> Withdrawn ${num}")
                transactions.insert(0, f"Withdrawn: ${num}")
            else:
                print("\t\t> A/C balance is low")

        case "3":
            print(f"\t> Your new Balance is: {balance}")

        case "4":
            for t in transactions:
                print(t)

        case _:
            print("\t> Invalid option.")

    print(msg)
    str = input("Enter your option: ")

print("\n === Thank you for using our services === \n")
