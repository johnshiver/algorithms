def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    seen = set()
    def area(grid, x, y):
        if not(0 <= x < len(grid) and 0 <= y < len(grid[0])
               and (x, y) not in seen and grid[x][y]):
            return 0
        seen.add((x, y))

        return 1 + area(grid, x - 1, y) + \
            area(grid, x + 1, y) + \
            area(grid, x, y + 1) + \
            area(grid, x, y - 1)

    return max([area(grid, x, y)
                for x in range(len(grid))
                for y in range(len(grid[0]))])


if __name__ == "__main__":
    grid = [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]
    print maxAreaOfIsland(grid)
