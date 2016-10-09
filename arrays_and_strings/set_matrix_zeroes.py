"""
problem prompt taken from Cracking Code Interview 6th Ed.
"""


def set_zeroes(matrix):
    cols = []
    set_row = False
    for r in range(len(matrix)):
        row = matrix[r]
        # figure out which columns have 0's
        for i in range(len(row)):
            if row[i] == 0:
                cols.append(i)
                set_row = True
            if set_row:
                # set entire row to 0
                matrix[r] = map(lambda x: 0, row)
                set_row = False

    cols = set(cols)
    for row in matrix:
        for i in cols:
            row[i] = 0
    return matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 0],
        [1, 1, 1, 1, 1]
    ]

    print(matrix)
    set_zeroes(matrix)
    print(matrix)
