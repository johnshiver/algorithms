
def selection_sort(input_list):
    """Very simple sorting algorithm.

    Selection sort selects one element at a time,
    compares it to all other elements in the list

    The correct position for that selected element is found
    before moving on to the next element

    After each pass, the list is sorted that much more
    (e.g. after 3 loops, the first 3 elements will be sorted)

    Complexity: O(n^2) in the worst case
         -  in worst case, "n" elements are checked for every selected element

    Stable: Not stable
         - entities which are equal might be re-arranged

    Memory: O(1)
        - sorts in place, original list re-used so no extra space

    Adaptivity: NO
        - no way to know if entire list is sorted so
          no way to break out of the loop early

    Discussion:
      - not really many use cases for this sort algo given that
        it's O(n^2) and not adaptive
      - biggest advantage is the O(1) memory

    Args:
        input_list (int)
    Returns:
        sorted list
    """
    for i in range(len(input_list)):
        # note: must be i+1, otherwise you will loop back to already sorted items
        for j in range(i+1, len(input_list)):
            if input_list[i] > input_list[j]:
                input_list[j], input_list[i] = input_list[i], input_list[j]

    return input_list
