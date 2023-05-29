#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Variable to keep track of the number of integers printed

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except IndexError:
        pass  # Ignore index errors when x is larger than the list length

    print()  # Print a new line after the integers are printed
    return count
