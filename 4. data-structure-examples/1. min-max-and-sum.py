list1 = [20, 40, 10, 50, 30]

total = 0
max = list1[0]  # assume 1st element is the biggest (for now)
min = list1[0]  # assume 1st element is the smallest (for now)

for i in list1:
    total += i
    if i > max:
        max = i
    if i < min:
        min = i

print(f"sum = {total}")
print(f"max = {max}")
print(f"min = {min}")
