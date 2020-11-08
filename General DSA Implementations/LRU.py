# A node is created for each key that is currently in our cache
class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next
    
    def __str__(self):
        prev = next = "None"
        if self.prev is not None:
            prev = str(self.prev.key)
        if self.next is not None:
            next = str(self.next.key)

        return "Node #" + str(self.key) + " has prev: #" + prev + ", next: #" + next

# Used for O(1) remove from front, append
class DLL:
    def __init__(self):
        self.head = self.tail = None 
    
    def add_to_front(self, node):
        if self.head is None and self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = None
            self.head.prev = node
            self.head = node

    def add_to_end(self, node):
            self.head = self.tail = node 
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
        
    def set_as_head(self, node):                            # Given a node currently in the DLL, set it as head
        self.remove(node)            
        self.add_to_front(node)
        
    # Given a node currently in the DLL, set it as head
    def set_as_tail(self, node):
        self.remove(node)
        self.add_to_end(node)

    def remove(self, node):
        # The DLL only contains this node and is now empty
        if node == self.head and node == self.tail:
            self.head = self.tail = None
        
        # We are removing the head node, set the next node as new head
        elif node == self.head:
            node.next.prev = None
            self.head = node.next
        
        # We are removing the tail node, set the prev node as the new tail 
        elif node == self.tail:
            node.prev.next = None
            self.tail = node.prev
        
        # The node is somewhere in the middle of our DLL
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            
    def __str__(self):
        print("Printing DLL with head:", self.head, "and tail", self.tail)
        
        output_str = ""
        current_node = self.head
        while current_node is not None:
            output_str += (str(current_node.key) + " <-> ") 
            current_node = current_node.next

        return output_str

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_vals = {}                                  # Maps key -> to [val, reference to Node (that represents the key)]
        self.dll = DLL()
    
    def get(self, key: int) -> int:
        if key not in self.key_vals:
            return -1
       
        val, key_node = self.key_vals[key]       
        self.dll.set_as_head(key_node)                  # Set the key as MRU
        
        # print("After get(", key, ")")
        # print(self.key_vals)
        # print(self.dll)
        # print("----------\n")

        return val
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_vals:
            self.key_vals[key][0] = value                   # Update the value of the existing key
            key_node = self.key_vals[key][1]            
            self.dll.set_as_head(key_node)                  # Set the associated node as MRU
            
        elif len(self.key_vals) != self.capacity:
            key_node = Node(key)                            # We are inserting a key for the first time, and the cache isn't full
            self.dll.add_to_front(key_node)                 # Use the DLL as FIFO, add the new key to the front since it's now MRU
            self.key_vals[key] = [value, key_node]          # Save the value and a reference to the associated node

        else:                                               # We are inserting a new key and cache is full, delete LRU
            evicted_node = self.dll.tail
            self.dll.remove(evicted_node)
            del self.key_vals[evicted_node.key]             # Delete the (key, val) pair of the evicted key

            # Add in the new (key, val) pair
            key_node = Node(key)
            self.key_vals[key] = [value, key_node]
            self.dll.add_to_front(key_node)                 # Set the new (key, val) as the MRU
            
        # print("After put(", key, ",", "val",")")
        # print("Tail is,", self.dll.tail.key)
        # print(self.dll)
        # print(self.key_vals)
        # print("----------\n")


# lru = LRUCache(2)                
# lru.put(2,1)
# lru.put(3,2)                 
# lru.get(2)
# lru.put(4,3)
# lru.get(2)

# lru = LRUCache(2)
# lru.put(2,1)
# lru.put(1,1)
# lru.put(2,3)
# lru.put(4,1)


# one = Node(1)
# two = Node(2)
# three = Node(3)

# dll = DLL()
# dll.add_to_front(one)
# dll.add_to_front(two)
# dll.add_to_front(three)
# print(dll)
# dll.remove(two)
# print(dll)


# ["LRUCache","put","put","put","put","get","get"]
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]



# lru = LRUCache(2)
# lru.put(2,1)
# lru.put(1,1)
# lru.put(2,3)
# lru.put(4,1)


lru = LRUCache(1)
lru.put(2,2)
lru.put(1,1)
lru.get(1)