"""
problem take from cracking the coding interveiw

9.2 Imagine a robot sitting on the upper left corner of an X by Y grid.
The robot can only move in two directions; right and down. How many possible
paths are there for the robot to go from (0,0) to (x,y)?

FOLLOW UP:
Imagine certain spots are off limits, such that the robot cannot step
on them. Find a path from the robot from top left to bottom right corner.
"""

import functools

def memoize(f):
    cache = {}
    @functools.wraps(f)
    def memf(*args, **kwargs):
        fkwargs = frozenset(kwargs.items())
        if (args, fkwargs) not in cache:
            cache[args, kwargs] = f(*args, **kwargs)
        return cache[args, fkwargs]
    return memf


class Grid(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.forbidden_coords = set()

    def mark_as_forbidden(self, row, column):
        self.forbidden_coords.add((row, column))

    def is_allowed(self, row, column):
        """
        Check whether (row, column) is a valid spot.

        Return True if (row, column) is inside the bounds
        of the grid and has not been marked as off-limits.
        """

        return (0<= row    < self.x and
                0<= column < self.y and
                (row, column) not in self.forbidden_coords)

    @memoize
    def find_path(self, row=0, column=0):
        """
        Return the path from (row, column) to (x-1, y-1)

        Finding a path from (x, y) to the destination is the same
        as moving to its two neighbors (x-1, y) and (x, y-1_ and
        finding the path from there. We keep doing this until
        a path reaches the destination. Always try the right neighbor
        first, then if no valid solution exists, the bottom one.
        If the destination cannot be reached, we backtrack returning None.
        """

        destination = (self.x-1, self.y-1)
        current = [(row, column)]

        if (row, column) == destination:
            return current

        neighbors = []
        neighbors.append((row, column+1))
        neighbors.append((row+1, column))

        for n in neighbors:
            if self.is_allowed(*n):
                path = self.find_path(*n)
                # subpath reaches bottom right
                if path and path[-1] == destination:
                    return current + path

