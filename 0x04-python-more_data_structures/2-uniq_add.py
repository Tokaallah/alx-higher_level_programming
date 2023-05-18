#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()
    
    # Iterate over each element in the input list
    for num in my_list:
        # Check if the element is an integer
        if isinstance(num, int):
            # Add the integer to the set
            unique_integers.add(num)
    
    # Compute the sum of the unique integers
    sum_unique_integers = sum(unique_integers)
    
    return sum_unique_integers
