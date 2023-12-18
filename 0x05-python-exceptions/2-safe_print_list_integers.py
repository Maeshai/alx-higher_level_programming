#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    printed_count = 0
    for element in my_list[:x]:
        if isinstance(element, int):
            print(f"{element}", end="")
            printed_count += 1
    print()
    return printed_count
