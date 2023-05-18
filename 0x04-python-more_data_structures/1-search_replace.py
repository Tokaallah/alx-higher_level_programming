#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new_list = []
    
    # Iterate over each element in the input list
    for element in my_list:
        # Check if the element matches the search value
        if element == search:
            # Replace the element with the replace value
            new_list.append(replace)
        else:
            # Keep the original element
            new_list.append(element)
    
    return new_list
