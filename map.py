
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

    def get(self, key):
        start = self.hash_function(key, self.size)

        data = None
        stop = False
        found = False
        position = start
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position is start:
                    stop = True
        return data

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash+1) % self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
