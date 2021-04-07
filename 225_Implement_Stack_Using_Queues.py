class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

# Using DLL implementation
class Q:
    def __init__(self):
        # Use dummy head and tail nodes
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
        
    def enQ(self, val):
        # Update pointers
        oldTail = self.tail.prev
        newNode = Node(val)
        oldTail.next = newNode
        newNode.next = self.tail
        
        # Add the node as the tail
        self.tail.prev = newNode
        self.size += 1

    def deQ(self):
        if(self.isEmpty()):
            return None
        
        # Update pointers
        firstNode = self.head.next
        secondNode = firstNode.next
        self.head.next = secondNode
        secondNode.prev = self.head 
        
        # Remove the first node from the front of the list
        firstNode.next = firstNode.prev = None        
        self.size -= 1
        return firstNode.val
        
    def peek(self):
        return self.head 

    
class MyStack:
    def __init__(self):
        self.q1 = Q()
        self.q2 = Q()
        self.topVal = None
        self.size = 0
        
    def push(self, x: int) -> None:
        self.q1.enQ(x)
        self.topVal = x
        self.size += 1

    def pop(self) -> int:
        if(self.size == 0): return None
        if(self.size == 1):
            self.topVal = None
            self.size = 0
            return self.q1.deQ()
        
        # Transfer all elements to the second queue except the last 2 (the top 2)
        while self.q1.size > 2:
            curr = self.q1.deQ()
            self.q2.enQ(curr)
        
        # Assign the 2nd to last element as the new top of the stack before moving to second queue
        self.topVal = self.q1.deQ()
        self.q2.enQ(self.topVal)
        
        # Remove and return the last element in the first queue (top of stack), swap queue back
        poppedElem = self.q1.deQ()
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        self.size -= 1
        
        return poppedElem

    def top(self) -> int:
        return self.topVal

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()