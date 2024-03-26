try:
    num = 10
    lst = [0, 10, 20, 30]

    index = int(input('Enter an index: '))  # "ValueError"

    selected_number_from_list = lst[index]  # possible chance of "IndexError"
    print(f'selected number is: {selected_number_from_list}')

    result = num / selected_number_from_list    # possible chances of "ZeroDivisionError"
    print(f'result = {result}')
except ValueError:
    print('Invalid integer')
except IndexError:
    print('Please type integer between 0 to 3')
except ZeroDivisionError:
    print('You cannot divide by 0, please select another index.')
except:
    print('unexpected error occurred')
finally:
    print("Thank you for our using our services")