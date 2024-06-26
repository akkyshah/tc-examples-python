def add_2_number(x, y = 1000, /):
    n = x + y
    return n

n = add_2_number(100, 200)
print(n)
n = add_2_number(100)
print(n)
n = add_2_number(100, 200)
print(n)