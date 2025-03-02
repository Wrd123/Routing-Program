# hash_table.py
# Class implementing a hash table using separate chaining.
class ChainingHashTable:
    # Initializes the hash table with an optional capacity.
    # Each bucket is initially set to an empty list.
    def __init__(self, initial_capacity=10):
        # Create a table of empty lists representing buckets.
        self.table = []
        for _ in range(initial_capacity):
            self.table.append([])

    # Inserts a new key-item pair or updates the value if the key already exists.
    def insert(self, key, item):
        # Determine the bucket index for the given key.
        bucket_index = hash(key) % len(self.table)
        bucket = self.table[bucket_index]

        # Check if the key already exists in the bucket and update its value.
        for pair in bucket:
            if pair[0] == key:
                pair[1] = item
                return True

        # If the key is not found, add the new key-item pair to the bucket.
        bucket.append([key, item])
        return True

    # Searches for a value by key in the hash table.
    # Returns the associated item if found; otherwise, returns None.
    def search(self, key):
        # Compute the bucket index for the given key.
        bucket_index = hash(key) % len(self.table)
        bucket = self.table[bucket_index]

        # Look for the key within the bucket.
        for pair in bucket:
            if pair[0] == key:
                # Return the associated value if the key is found.
                return pair[1]

        # Return None if the key does not exist in the table.
        return None
