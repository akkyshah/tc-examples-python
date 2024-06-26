def add_number(*nums):
    n = 0
    for number in nums:
        n += number
    return n

result = add_number(100, 200)
print(result)
result = add_number(100, 200, 300)
print(result)
result = add_number(100, 200, 300, 400, 500, 600, 700)
print(result)