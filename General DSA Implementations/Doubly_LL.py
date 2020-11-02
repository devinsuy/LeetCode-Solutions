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
            node.next = self.head
            self.head.prev = node
            self.head = node

    def add_to_end(self, node):
        if self.head is None and self.tail is None:
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
    


one = Node("1")
two = Node("2")
three = Node("3")
zero = Node("0")

dll = DLL(one)
dll.add_to_end(two)
dll.add_to_front(zero)
dll.add_to_end(three)
dll.set_as_tail(two)
# dll.set_as_head(two)


print(dll)