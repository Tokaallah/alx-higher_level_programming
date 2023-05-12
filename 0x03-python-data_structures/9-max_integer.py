#!/usr/bin/python3
def max_integer(my_list=[]):
    # Return None if the list is empty
    if len(my_list) == 0:
        return None
    
    # Initialize the max value to the first element of the list
    max_value = my_list[0]
    
    # Loop through the rest of the list
    for i in range(1, len(my_list)):
        # Update the max value if the current element is larger
        if my_list[i] > max_value:
            max_value = my_list[i]
    
    return max_value
