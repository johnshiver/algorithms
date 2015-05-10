
class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [[] for x in range(self.size)]
        self.data = [None for x in range(self.size)]

    def put(self, key, data):
        hash_val = self.hash_function(key, self.size)

        if self.slots[hash_val] is None:
            self.slots[hash_val] = key
            self.data[hash_val] = data
        else:
            next_slot = self.rehash(hash_val)
            while not self.slots[next_slot] and self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot)

        if self.slots[next_slot] is None:
            self.slots[next_slot] = key
            self.data[next_slot] = data
        else:
            self.data[next_slot] = data  # replace the current value

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash+1) % self.size