class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

class Stack:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def push(self, data):
        oldTail = self.tail.prev
        newTail = Node(data)
        
        # Update pointers
        oldTail.next = newTail
        newTail.prev = oldTail
        newTail.next = self.tail
        self.tail.prev = newTail
        self.size += 1
    
    def pop(self):
        if(self.size == 0):
            return None
        
        # Update pointers
        lastNode = self.tail.prev
        newLastNode = lastNode.prev
        newLastNode.next = self.tail
        self.tail.prev = newLastNode
        
        # Remove from list and return
        lastNode.next = lastNode.prev = None
        self.size -= 1        
        return lastNode.data 
    
    def peek(self):
        if(self.size == 0):
            return None
        else:
            return self.tail.prev.data
    
    def isEmpty(self):
        return self.size == 0
        
        
class MyQueue:
    
    def __init__(self):
        self.stPush = Stack()
        self.stPop = Stack()
        self.size = 0
        

    def push(self, x: int) -> None:
        self.stPush.push(x)
        self.size += 1
    
    def transferElems(self):
        while not self.stPush.isEmpty():
            self.stPop.push(self.stPush.pop())

    def pop(self) -> int:
        if(self.size == 0):
            return None
        
        # Transfer all elements from the push stack to the pop stack
        if(self.stPop.size == 0):
            self.transferElems()

        # Elements have been added to the push stack in reverse order
        # they have gone from LIFO to FIFO and can be popped
        self.size -= 1
        return self.stPop.pop()
        

    def peek(self) -> int:
        if(self.size == 0):
            return None
        if(self.stPop.size == 0):
            self.transferElems()
        return self.stPop.peek()
        

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()