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
        self.count = 0
        self.is_resized: False

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        hashed_key = 5381
        for char in key:
            hashed_key = hashed_key * 33 + ord(char)
        return hashed_key

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hashed_key = 5381
        for char in key:
            hashed_key = hashed_key * 33 + ord(char)
        return hashed_key

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hashed_index = self._hash_mod(key)

        if not self.storage[hashed_index]:
            self.storage[hashed_index] = LinkedPair(key, value)
        else:
            p = self.storage[hashed_index]
            if p.next == None:
                if p.key == key:
                    p.value = value
            else:
                while p.next:
                    if p.key == key:
                        p.value = value
                    p = p.next
            p.next = LinkedPair(key, value)

        self.count += 1

        # if self.count / len(self.storage) > 0.7:
        #     self.resize()

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_index = self._hash_mod(key)
        value = self.retrieve(key)

        if not self.storage[hashed_index]:
            print("Error: there is no such value")
        elif self.storage[hashed_index].value == value:
            self.storage[hashed_index] = self.storage[hashed_index].next
            self.count -= 1
        else:
            parent = self.storage[hashed_index]
            current_node = self.storage[hashed_index].next

            while current_node:
                if current_node.value == value:
                    parent.next = current_node.next
                    self.count -= 1
                    return
                current_node = current_node.next

            print("Error: there is no such value")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_index = self._hash_mod(key)

        if not self.storage[hashed_index]:
            return None
        else:
            current_node = self.storage[hashed_index]
            while current_node:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #new_capacity = len(self.storage) * 2

        # temporary_storage = [None] * len(self.storage)
        temporary_storage = HashTable(len(self.storage) * 2)
        current_pair = None
        for i in range(len(self.storage)):
            #temporary_storage[i] = self.storage[i]
            current_pair = self.storage[i]
            while current_pair is not None:
                temporary_storage.insert(current_pair.key, current_pair.value)
                current_pair = current_pair.next
        print(len(self.storage), '22')
        self.capacity = temporary_storage.capacity
        self.storage = temporary_storage.storage
        print(len(self.storage), '3333')
        return temporary_storage



       # self.storage = [None] * self.capacity
       # self.count = 0
     #   self.is_resized = True

       # for i in range(len(temporary_storage)):
           # if temporary_storage[i]:
           #     self.insert(temporary_storage[i].key,
           #                 temporary_storage[i].value)
           #     p = temporary_storage[i].next
           #     while p:
              #      self.insert(temporary_storage[i].key,
              #                  temporary_storage[i].value)
            #        p = p.next
      #  return temporary_storage


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
