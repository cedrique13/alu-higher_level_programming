#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list safely.
    
    Args:
        my_list (list): The list to print from.
        x (int): Number of elements to print.
    
    Returns:
        int: Number of elements actually printed.
    """
    printed_count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            printed_count += 1
    except IndexError:
        pass
    print()
    return printed_count
