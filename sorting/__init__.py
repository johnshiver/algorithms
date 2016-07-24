"""
# Reference: many notes taken from Udemy "break away coding interviews" class

Sorting Algorithms: Trade offs and considerations

1. Complexity of the algorithm used
  - how does it scale as the input size increases
2. Space
  - does it need extra space to hold information during sorting?
3. Stable
  - do equal elements maintain their original order after sorting?
    if yes, algo is said to be stable
  - depending on use case for sort, you might require equal elements maintain their original order,
    in which case, you need stable algorithm
4. Number of comparisons and swaps that are needed
  - does the algorithm work better with nearly sorted lists?
  - consider whether you know input list will be nearly sorted
5. Adaptive
  - as list gets into more sorted state, is algo smart enough to break early
    when the list is sorted, or does it need to go through every iteration?
"""


from .bubble_sort import bubble_sort
from .selection_sort import selection_sort
from .shell_sort import shell_sort
from .insertion_sort import insertion_sort
from .merge_sort import merge_sort
from .quick_sort import quick_sort
