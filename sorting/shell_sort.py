

def shell_sort(input_list):
    """
    Shell sort partitions the original list into
    sub-lists where a sub-list is made of elements
    separated by an 'increment'

    If increment is 2, then sublist is 2, 4, 6 and so on.

    Each sub-list is then sorted using insertion sort

    Increment is slowly reduced till it's 1

    The advantage is you are eventually applying insertion sort
    to a nearly sorted list, which is very efficient.
    """
