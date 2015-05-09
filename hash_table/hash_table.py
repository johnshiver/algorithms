"""
Hash Table Implementation

Data structure that can be searched in O(1)
"""


class HashTable(object):
    u"""
    Simple implementation of Hash table
    """
    def __init__(self):
        self.table = []

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

    def 

