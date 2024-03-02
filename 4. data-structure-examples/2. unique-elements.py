cars = ["BMW", "Ferrari", "Volvo", "BMW", "Mazda", "Volvo", "Porsche", "Ferrari", "BMW", "Dodge", "Volvo"]

unique = []	# empty list

for car in cars:
        if car not in unique:
                unique.append(car)		# append car in unique only if it does not already exist

print(unique)