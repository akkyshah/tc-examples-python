year = 2020
colors = ["Red", "Blue", "Yellow"]
lst = colors

lst[1] = "Purple"   
print(lst)      # [ "Red", "Purple", "Yellow" ]
print(colors)   # [ "Red", "Purple", "Yellow" ]

car = { "name": "BMW", "colors": colors, "year": year }
year = 1990     # Does not modify car since year (primitive) was copied
print(car)      # print key-values of car (where year is still 2020)

car["year"] = 2023
print(car)      # print key-values of car (where year is now 2023)

colors[2] = "Green"
print(lst)      # [ "Red", "Purple", "Green" ]
print(colors)   # [ "Red", "Purple", "Green" ]
print(car)      # print key-values of car (car["colors"] has "Green" in list)

car["colors"][0] = "Orange"
print(lst)      # [ "Orange", "Purple", "Green" ]
print(colors)   # [ "Orange", "Purple", "Green" ]
print(car)      # print key-values of car (car["colors"] has "Orange" in list)

del lst
print(colors)   # ["Red", "Purple", "Green"]
print(car)      # prints car (dictionary) JSON

car["specs"] = { "rimColors": ["blue", "black"], "rimType": "Steel" }
print(car)      # prints car (dictionary) JSON with "specs"

colors.clear()
print(car)      # prints car (dictionary) JSON with [] colors

del colors
print(car)      # prints car (dictionary) JSON with [] colors

car["colors"] = ["Red", "Purple", "Green"]
del car["specs"]["rimColors"]
print(car)      # prints car (dictionary) JSON with colors list

del car["specs"]
print(car)      # prints car (dictionary) JSON without specs


# 1. Primitives (int, float, boolean) are passed by Values
# 2. Complex (data-structures) are passed by reference
