
print("\n === Welcome to our Bank === \n")

balance = 0
msg = "\n1. Deposit \n2. Withdraw \n3. Check balance \n0. Quit\n"
print(msg)
str = input("Enter your option: ")

while str != "0":
    match str:
        case "1":
            num = int(input("\tEnter amount: "))
            balance += num
            print(f"\t\t> Deposited: ${num}")

        case "2":
            num = int(input("\tEnter amount: "))
            if (balance - num) < 0:
                print("\t\t> A/C balance is low")
            else:
                balance -= num
                print(f"\t\t> Withdrawn ${num}")

        case "3":
            print(f"\t> Your new Balance is: {balance}")

        case _:
            print("\t> Invalid option.")

    print(msg)
    str = input("Enter your option: ")

print("\n === Thank you for using our services === \n")
