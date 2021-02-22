class Node:
    def __init__(self, key=-1, val=-1):
        if(key == -1):
            self.isDummy = True
        else:
            self.key = key
            self.val = val
            self.isDummy = False
        self.prev = self.next = None
        
class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head 
        self.keys = set([])
    
    def addLast(self, node: Node) -> None:
        prevLast = self.tail.prev
        prevLast.next = node
        node.prev = prevLast
        node.next = self.tail
        self.tail.prev = node
        self.keys.add(node.key)
        
    def addFirst(self, node: Node) -> None:
        prevFirst = self.head.next
        prevFirst.prev = node
        node.next = prevFirst
        node.prev = self.head
        self.head.next = node
        self.keys.add(node.key)
    
    # Given a key, return the node with the matching key
    def getNode(self, key: int) -> Node:
        curr = self.head.next
        while(curr.key != key):
            curr = curr.next
        return curr
    
    def removeNode(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        
        node.prev = node.next = None
        self.keys.remove(node.key)
        
    def remove(self, key: int) -> None:
        node = self.getNode(key)
        self.removeNode(node)
    
    # Return whether or not a node with the key exists
    def hasKey(self, key: int) -> bool:
        return key in self.keys        
    
    def isEmpty(self) -> bool:
        return self.head.next.isDummy
    

class MyHashMap:
    # Double the hashmap size at 75% load capacity
    def getResize(self) -> int:
        return int(self.capacity * 0.75)
    
    def initBuckets(self) -> None:
        buckets = []
        for _ in range(self.capacity):
            buckets.append(DLL())
        return buckets
    
    def resize(self) -> None:
        # Load size reached, double buckets and copy data over
        self.capacity *= 2  
        self.maxLoad = self.getResize()
        prevBuckets = self.buckets
        self.buckets = self.initBuckets()
        
        # Copy all previous values into the new buckets
        for bucket in prevBuckets:
            if(not bucket.isEmpty()):
                curr = bucket.head.next
                while(not curr.isDummy):
                    newBucket = self.getBucket(curr.key)
                    newBucket.addLast(curr)
                    curr = curr.next
    
    def __init__(self):
        self.size = 0
        self.capacity = 16
        self.maxLoad = self.getResize()
        self.buckets = self.initBuckets()
        
    def getBucket(self, key: int) -> DLL:
        bucketIndex = hash(key) % (self.capacity - 1)
        return self.buckets[bucketIndex]

    def put(self, key: int, value: int) -> None:
        currBucket = self.getBucket(key)
        
        # Update the value of a previously inserted key
        if(currBucket.hasKey(key)):
            node = currBucket.getNode(key)
            node.val = value
            
        # Add a key,val pair for the first time
        else:
            self.size += 1
            
            # # Capacity reached, resize before insertion 
            # if(self.size == self.maxLoad):
            #     self.resize()
            #     currBucket = self.getBucket(key)
                
            node = Node(key, value)
            currBucket.addFirst(node)

    def get(self, key: int) -> int:
        currBucket = self.getBucket(key)
        
        if(currBucket.hasKey(key)):
            node = currBucket.getNode(key)
            return node.val
        else:
            return -1      

    def remove(self, key: int) -> None:
        currBucket = self.getBucket(key)
        if(currBucket.hasKey(key)):
            currBucket.remove(key)
            self.size -= 1
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)