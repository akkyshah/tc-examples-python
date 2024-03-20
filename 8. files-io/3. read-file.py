f = open("sample.txt", "r")  # Default opens with "r" option - i.e. - Read Text | throws error if the file does not exist

# data = f.read(10)  # reads 10 characters
# print(data)

# data = f.readline()  # reads 1 line.
# print(data)


for line in f:  # you can also loop on file. Python will iterate on lines - i.e. - it will read line-by-line
    print(line, end="")

# print(f.read())  # reads everything

f.close()   # good practice - you must always close the file.