n = int(input("Enter a number: "))
result = True
for i in range(2, n):
    if n % i == 0:
        result = False
        break
if result == True:
    print(f"{n} is Prime")
else:
    print(f"{n} is not Prime")
