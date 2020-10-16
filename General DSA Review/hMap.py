# Modified HashMap Implementation
# -------------------------------
# NOTE: Problem description specifies that: 
#           - Only valid input will be passed
#           - Keys will be integers for addToKey() functionality
#               - (implementation works with non integers as well if addToKey() not called)
#           - Function should return the sum of all values retrieved from each get() operation

class hMap:
    def __init__(self):
        self.arr = [None] * 10                              # Default init size
        self.keys = set([])
        self.set_load()

    # Resizing bookkeeping
    def set_load(self):
        self.num_empty = len(self.arr)
        self.resize_amt = int(len(self.arr) * 0.25)         # Use a 75% load factor to resize the array 

    def need_resize(self):
        return self.num_empty == self.resize_amt 
    
    def remove(self, key):
        bucket_index = hash(key) % len(self.arr)
        remove_entry = (key, self.get(key))                 

        self.arr[bucket_index].remove(remove_entry)

    def insert(self, key, val):
        bucket_index = hash(key) % len(self.arr)

        if self.arr[bucket_index] is None:                 
            self.arr[bucket_index] = set([(key, val)])      # (key, value) stored as immutable, hashable Tuple type
            self.num_empty -= 1
            self.keys.add(key)
            if self.need_resize():                          # Check the number of empty buckets (i.e. if we have reached 75% load factor yet) 
                self.resize()

        # Add our (key, val) to the corresponding bucket
        else:                                               
            if key in self.keys:                            # key is an existing key, overwrite the value by removing the existing (key, val) entry first
                self.remove(key)
            else:
                self.keys.add(key)    

            self.arr[bucket_index].add((key, val))
            
    def get(self, key):
        bucket_index = hash(key) % len(self.arr)

        # Iterate over the bucket until we find the corresponding (key, val), return val
        for key_val in self.arr[bucket_index]:
            if key_val[0] == key:
                return key_val[1]

    def addToValue(self, add_val):
        for key in self.keys:                               # Add add_val to the value that each key maps to
            a = self.get(key) + add_val
            self.insert(key, self.get(key) + add_val)

    def addToKey(self, add_val):
        keys = [None] * len(self.keys)
        vals = [None] * len(self.keys)
        key_val_ptr = 0

        # Retrieve the existing (key, val) pairs O(keys*max_bucket_size)
        for key in self.keys:
            keys[key_val_ptr] = key
            vals[key_val_ptr] = self.get(key)
            key_val_ptr += 1
        
        self.arr = [None] * len(self.arr)
        new_keys = set([])
        self.set_load()
        
        # Reinsert our values with the incremented key O(keys)
        for i in range(len(keys)):
            new_key = keys[i] + add_val
            self.insert(new_key, vals[i])
            new_keys.add(new_key)
        
        self.keys = new_keys

    # Double the size of the array, copy entries into new array
    def resize(self):
        print("Resize called")
        keys = [None] * len(self.keys)
        vals = [None] * len(self.keys)
        key_val_ptr = 0
        
        # Retrieve the (key, val) pairs from the old array O(keys*max_bucket_size)
        for key in self.keys:
            keys[key_val_ptr] = key
            print("Retrieving value with key", key)
            vals[key_val_ptr] = self.get(key)
            key_val_ptr += 1

        self.arr = [None] * (len(self.arr) * 2)
        self.set_load()

        # Copy each (key, value) into the newly resized array O(keys)
        for i in range(len(keys)):
            self.insert(keys[i], vals[i])


# Perform HashMap operations, increment retrieved_sum with the value
# retrieved from each get() operation, return retrieved_sum
def run_queries(queryTypes, queries, output=False):
    hm = hMap()
    retrieved_sum = 0
    
    for i in range(len(queryTypes)):        # Process queries
        current_type = queryTypes[i]
        current_query = queries[i]

        if current_type == "insert":
            hm.insert(current_query[0], current_query[1])
        elif current_type == "addToValue":
            hm.addToValue(current_query[0])
        elif current_type == "addToKey":
            hm.addToKey(current_query[0])
        elif current_type == "get":
            retrieved_sum += hm.get(current_query[0])
        else:
            print("Invalid query type \"" + current_type + "\"", "for query:", current_query, "skipping ...")

        if output:  # Print the underlying array after each operation
            print("After query #" + str(i) + ":", hm.arr)

    return retrieved_sum


#---------------------- CodeSignal Cases ----------------------

class InputCase:
    def __init__ (self, queryTypes, queries, expected_output):
        self.queryTypes = queryTypes
        self.queries = queries
        self.expected_output = expected_output

input_cases = [
    InputCase(
        ["insert", "insert", "addToValue", "addToKey", "get"],
        [[1,2], [2,3], [2], [1], [3]],
        5
    ),
    InputCase(
        ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"],
        [[1,2], [2], [1], [2,3], [1], [-1], [3]],
        6
    ),
    InputCase(
        ["addToKey", "addToKey", "insert", "addToValue", "addToValue", "get", "addToKey", "insert", "addToKey", "addToValue"],
        [[-3], [-1], [0,-3], [3], [-1], [0], [-1], [-4,-5], [-1], [-4]],
        -1
    ),
    InputCase(
        ["insert", "insert", "addToKey", "addToKey", "addToKey", "insert", "addToValue", "addToKey", "addToKey", "get"],
        [[-5,-2], [2,4], [-1], [-3], [1], [3,-2], [-4], [-2], [2], [-8]],
        -6
    ),
    InputCase(
        ["insert", "get", "insert", "addToValue", "addToValue", "addToValue", "insert", "addToKey", "get", "insert"],
        [[2,1], [2], [1,3], [-1], [0], [3], [4,-5], [3], [4], [1,1]],
        6
    ),
    InputCase(
        ["insert", "insert", "insert", "get", "insert", "insert", "insert", "addToKey", "insert", "insert"],
        [[3,-4], [-4,3], [4,-3], [4], [-5,0], [-2,-5], [2,2], [1], [-5,-2], [1,3]],
        -3
    ),
    InputCase(
        ["addToValue", "addToKey", "addToKey", "insert", "addToValue", "addToValue", "insert", "get", "get", "insert"],
        [[-2], [-3], [0], [-3,1], [-2], [-4], [2,-4], [2], [2], [3,-1]],
        -8
    )
]


# ---------------------- Manual Testing ----------------------
# print("Expected:", input_cases[6].expected_output)
# print("Output:", run_queries(input_cases[6].queryTypes, input_cases[6].queries, output=True))

# ---------------------- Auto Testing ----------------------
import unittest

class TestCases(unittest.TestCase):
    def test_run(self):
        count = 1
        for case in input_cases:
            self.assertEqual(run_queries(case.queryTypes, case.queries), case.expected_output)
            print("Test case #" + str(count), "passed")
            count += 1

if __name__ == '__main__':
    unittest.main()