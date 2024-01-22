#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safely prints elements from a list up to the specified index.

    Args:
        my_list (list): The list to be printed.
        x (int): The index up to which elements should be printed.

    Returns:
        int: Total number of elements successfully printed.
    """

    total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            total += 1
        except IndexError:
            break
    print("")
    return(total)
