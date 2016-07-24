

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
    def modified_insertion_sort(list_to_sort, start, h):
        """
        Args:
             h (int): the increment. have to name it something else
                      so as not to interfere with outter scope
        """
        for i in range(start, len(list_to_sort), h):
            # start with the 'sorted list', look at next element, and count down
            # make sure not to include 0, because first element is always 'sorted'
            for j in range(start + h, i+h, h)[::-1]:
                if list_to_sort[j] < list_to_sort[j - h]:
                    list_to_sort[j - h], list_to_sort[j] = list_to_sort[j], list_to_sort[j - h]
                else:
                    break
        return input_list

    increment = len(input_list) / 2
    while increment >= 1:
        for start_index in range(increment):
            modified_insertion_sort(input_list, start_index, increment)
        increment /= 2

    return input_list
