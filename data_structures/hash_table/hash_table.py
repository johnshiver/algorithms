"""
Hash Table Implementation

Data structure that can be searched in O(1)

"""

import random


class HashTable(object):
    u"""
    Simple implementation of Hash table
    """
    def __init__(self, length, hash_method='mid_square'):
        self.table = [[] for i in range(length)]
        self.hash_method = self.mid_square_method

    def insert(self, value):
        if type(value) == str:
            hash_val = self.hash_string(value)
        else:
            hash_val = self.hash_method(value)
        slot = self.open_addressing_linear_proving(hash_val)
        return self.table[slot].append(value)

    # Hash Functions
    def remainder_method(self, value):
        u"""
        divides item by table size and returns the remainder
        as the hash value. very simple / not ideal because of
        high collision rate
        """
        return value % len(self.table)

    def folding_method(self, value):
        u"""
        Divide item into equal sized pieces (the last piece therefore
        may not be of equal size)
        Might be good for phone numbers.

        Example use for phone numbers:
           value = 212-234-3456
           make into groups:
               vals = (21, 22, 34, 34, 56)
               sum(vals) = 167
               167 mod length table = hash value
        """
        pass

    def mid_square_method(self, value):
        u"""
        Square the value then extract some portion of resulting digits
        """
        square = str(value**2)
        middle_two = int(square[(len(square) // 2) - 1: (len(square) // 2) + 1])
        return middle_two % len(self.table)

    def hash_string(self, string):
        u"""
        returns hash of a string with weighting
        """
        total = 0
        for c in range(len(string)):
            total += ord(string[c]) * (c+1)

        return total % len(self.table)

    # Collision resolutions
    def open_addressing_linear_proving(self, slot):
        u"""
        Tries to find next open slot or address in the hash table after collision
        by visiting each node until finding an open one
        *thid method succeptible to clustering
        """
        if len(self.table[slot]) == 0:
            return slot
        for i in range(len(self.table)):
            if len(self.table[i]) == 0:
                return i
        return random.choice(xrange((len(self.table)-1)))

    def open_addressing_rehashing(self, probe_length):
        u"""
        Tries to find next open slot or address in the hash table after collision
        by visiting every probe_length slot until one is open
        Example: if probe length is 3, will visit every third slot until
        there is an open one
        *thid method succeptible to clustering
        """
        pass

    def chaining_search(self):
        pass












