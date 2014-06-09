def bSearch(L, e):
    """
    Assumes L is a list, the elements of which are in ascending order.
    Returns True if e is in L and False othewrise
    """

    mid = L[-1] // 2
    high = L[-1]
    low = L[0]
    found = False
    while not found:
        if mid == e:
            found = True
        elif mid == low or mid == high:
            break
        elif e > mid:
            low = mid
        else:
            high = mid
        mid = (low + high) // 2

    return found
