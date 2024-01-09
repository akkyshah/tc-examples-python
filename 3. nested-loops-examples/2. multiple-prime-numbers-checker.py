n = int(input("Enter a number: "))

while n != 0:
    if n < 0:
        print("Invalid Input")
    elif n > 0:
        result = True
        for i in range(2, n):  # start=2  |  checks: i < n
            if n % i == 0:
                result = False
        if result == True:
            print(f"{n} is Prime")
        else:
            print(f"{n} is not Prime")

    n = int(input("\nEnter a number: "))

print("\n\nExiting program...")
