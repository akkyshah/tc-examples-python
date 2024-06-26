def is_prime(n):
    res = True
    for i in range(2, n):
        if n % i == 0:
            res = False
            break
    return res


def print_prime_numbers_till(n=10):  # parameter n's default value is 10
    print(f'\nPrinting prime numbers from 2 to {n}: ')
    for i in range(2, n + 1):
        result = is_prime(i)
        if result == True:
            print(i, end=", ")


print_prime_numbers_till()
print()
print_prime_numbers_till(500)
