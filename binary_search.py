# def bSearch(L, e):
#     """
#     Assumes L is a list, the elements of which are in ascending order.
#     Returns True if e is in L and False othewrise
#     """

#     mid = L[-1] // 2
#     high = L[-1]
#     low = L[0]
#     found = False
#     while not found:
#         if mid == e:
#             found = True
#         elif mid == low or mid == high:
#             break
#         elif e > mid:
#             low = mid
#         else:
#             high = mid
#         mid = (low + high) // 2

#     return found


def bSearch(L, e):
    """
    Assumes  L is a list, the elemnts of which are in ascended order
    Returns true if e is in L, and false otherwise
    """

    def binarySearch(L, e, low, high):
        if low == high:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        if L[mid] > e:
            if low == mid:
                return False
            else:
                return binarySearch(L, e, low, mid-1)
        else:
            return binarySearch(L, e, mid+1, high)

    if len(L) == 0:
        return False
    else:
        return binarySearch(L, e, 0, len(L) - 1)
