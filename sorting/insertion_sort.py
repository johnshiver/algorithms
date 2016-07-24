

def insertion_sort(input_list):
    """
    Start with a sorted sub-list of size 1 (list of 1 is always sorted)

    Insert the next element into the sorted sub-list at the correct position.
    Now the sorted sub-list has two elements

    Complexity: O(n^2) in the worst case
        - in worst case (list is sorted in descending order)
          "n" elements are checked and swapped for each selected
          element to get to the correct position

    Stable: Yes
        - logical ordering will be maintained

    Memory: O(1)
        - sorts in place, original list re-used so no extra space

    Adaptivity: YES
        - if there were no swaps when adding an element to list,
          then we can break out of comparing rest of the elements

    Number of comparisons and swaps:
        - O(n^2) comparisons and O(n^2) swaps
        - more swaps than selection sort!

    Discussion:
        - it has very low overhead and is traditionally the sort
          of choice when used with faster algorithms which follow
          a divide and conquer approach
        - why insertion sort over bubble sort?
          - bubble sort requires an additional pass over all elements
            to ensure that the list is fully sorted
          - bubble sort must do n comparisons at every step.
            insertion sort can stop comparison elements when the right
            position in the sorted list is found
          - bubble sort performs poorly with modern hardware because
            number of writes and swaps that it performs results in
            cache misses so has greater overhead than insertion sort
    """
    for i in range(len(input_list)):
        # start with the 'sorted list', look at next element, and count down
        # make sure not to include 0, because first element is always 'sorted'
        for j in range(1, i+1)[::-1]:
            if input_list[j] < input_list[j-1]:
                input_list[j-1], input_list[j] = input_list[j], input_list[j-1]
            else:
                break
    return input_list
