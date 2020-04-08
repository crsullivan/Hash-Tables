# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = len(self.storage)


    def _hash(self, key):
        for i in range(100000):
            hash_value = hash(key)
        return hash_value


    def _hash_djb2(self, key):
        hash = 5381
        for char in key:
            hash = (hash * 33) + ord(char)
        return hash % self.capacity


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def resize(self):
        self.capacity *= 2
        old_storage = self.storage
        new_storage = [None] * self.capacity
        self.storage = new_storage
        
        for i in range(len(old_storage)):
            if old_storage[i] is not None:
                pair = old_storage[i]
                while pair is not None:
                    self.insert(pair.key, pair.value)
                    pair = pair.next

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        i = self._hash_djb2(key)

        if self.storage[i] is not None:
            # collision
            new_pair = LinkedPair(key, value)
            new_pair.next = self.storage[i]
            self.storage[i] = new_pair
        else:
            self.storage[i] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        i = self._hash_djb2(key)
        pair = self.storage[i]

        if pair == None:
            print('Warning: key not found')

        while pair.key is not key:
            pair = pair.next

        if pair.value == None:
            return None
        else:
            pair.value = None

        return None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        i = self._hash_djb2(key)
        pair = self.storage[i]

        while pair is not None:
            if pair.key == key:
                return pair.value
            pair = pair.next
        
        return None




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
