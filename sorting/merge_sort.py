
def merge_sort(input_list):
    """
    Divide and conquer algorithm, creates smaller sub problems
    using recursion.

    A list is broken down into smaller and smaller lists until there
    are lists of length one.  We can consider lists of length one sorted.

    Merge the sorted lists back together to get the fully sorted list.

    Complexity: O(NLOGN)
        - log n divides to create the single element sorted lists
        - n merges to create the final sorted list
    Stable: Yes
        - logical ordering will be maintained
    Memory: O(N)
        - all the smaller lists we create in the divide phase
    Adaptivity: No
        -  merge sort doesnt know at any point whether the list is already sorted
           and will always go through the entire recursive call
    Discussion:
        - use merge sort when you need speed and have the resources
          for the memory overhead
    """

    def merge(list_to_sort, list_first_half, list_second_half):
        first_half_index = second_half_index = merge_index = 0

        while first_half_index < len(list_first_half) and second_half_index < len(list_second_half):
            if list_first_half[first_half_index] <= list_second_half[second_half_index]:
                list_to_sort[merge_index] = list_first_half[first_half_index]
                first_half_index += 1
            else:
                list_to_sort[merge_index] = list_second_half[second_half_index]
                second_half_index += 1
            merge_index += 1

        # it is possible that one of the lists is larger than the other
        # in which case, finish copying them over to the end of the list
        # note: only one of these should execute
        while first_half_index < len(list_first_half):
            list_to_sort[merge_index] = list_first_half[first_half_index]
            merge_index += 1
            first_half_index += 1
        while second_half_index < len(list_second_half):
            list_to_sort[merge_index] = list_second_half[second_half_index]
            merge_index += 1
            second_half_index += 1

        return list_to_sort

    # perform merge sort
    if len(input_list) <= 1:
        return input_list

    middle_index = len(input_list) / 2
    left = input_list[:middle_index]
    right = input_list[middle_index:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(input_list, left, right)
