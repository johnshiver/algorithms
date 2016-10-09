



def highest_product_of_three(l):
    """
    given list of integers, return
    highest product of three integers

    **can assume at least three integers
    """

    first, second = l[0], l[1]
    largest = max(first, second)
    second = min(first, second)
    highest = 0
    for n in l[2:]:
        highest = max(highest, largest*second*n)
        if n > largest:
            largest, second = n, largest
        elif n > second:
            second = n
    return highest


if __name__ == "__main__":
    x = [1, 2, 4, 3, 2, 3, 3, 4, 5]
    ans = 60
    res = highest_product_of_three(x)
    print(res, res == 80)
