
def bubble_sort(input_list):
    """
    The smallest element bubbles to the correct position
    by comparing adjacent elements.

    For each iteration, every element is compared with its neighbor
    and swapped if they arent in the right order.

    Smallest elements 'bubble' to the beginning of the list.

    At the end fo the first iteration, the smallest element is in the
    right position, at the end of the second iteration, the second
    smallest is in the right position and so on

    Complexity: O(n^2) in the worst case
        - in worst case (list is sorted in descending order)
          "n" elements are checked and swapped for each selected
          element to get to the correct position

    Stable: Yes
        - logical ordering will be maintained

    Memory: O(1)
        - sorts in place, original list re-used so no extra space

    Adaptivity: YES
        - if there were no swaps on an iteration, we know the list
          is already sorted, and we can break out early

    Number of comparisons and swaps:
        - O(n^2) comparisons and O(n^2) swaps
        - more swaps than selection sort!

    Discussion:
        - O(n^2) == bad
        - advantage over selection sort: adaptivity
    """
    for i in range(len(input_list)):
        swapped = False
        # again, i represents the last position in list that is sorted
        for j in range(len(input_list) - 1, i, -1):
            if input_list[j] < input_list[j-1]:
                input_list[j-1], input_list[j] = input_list[j], input_list[j-1]
                swapped = True
        # if no swaps, list is already in sorted state and we can break out
        if not swapped:
            break
    return input_list

