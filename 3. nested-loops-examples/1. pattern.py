for i in range(1, 10):

    spaces = (10 - i) * 2 * " "
    print(spaces, end="")

    for j in range(1, i):
        print(f"{j} ", end="")

    for j in range(i, 0, -1):
        print(f"{j} ", end="")

    print()
