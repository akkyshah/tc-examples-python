f = open('sample.txt', 'a')     # 'w' stands for write-in-overwrite mode | creates the file if it does not exist
for i in range(1, 10):
    f.write('Hello World-' + str(i) + '\n')
f.close()

# f = open('sample.txt', 'w')     # 'w' stands for write-in-overwrite mode | creates the file if it does not exist
# for i in range(1, 10):
#     f.write('Hello World!' + '\n')
# f.close()
