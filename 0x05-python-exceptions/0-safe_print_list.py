#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0  # Variable to keep track of the number of elements printed

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # Ignore index errors when x is larger than the list length

    print()  # Print a new line after the elements are printed
    return count

