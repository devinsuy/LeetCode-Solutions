import java.util.PriorityQueue;
import java.util.HashMap;

class Node {
    public Node next;
    public Node prev;
    public int key;
    public int val;
    public int count;
    public boolean isDummy;
    
    public Node(){
        this.isDummy = true;
        this.next = this.prev = null;
    }
    
    public Node(int key, int val){
        this.isDummy = false;
        this.key = key;
        this.val = val;
        this.next = this.prev = null;
    }
}

class DLL{
    public Node head;
    public Node tail;
    
    public DLL(){
        this.head = new Node();
        this.tail = new Node();
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }
    
    public void addFirst(Node n){
        // There are no existing nodes in the list
        if(this.head.next.isDummy){
            this.head.next = n;
            n.prev = this.head;
            n.next = this.tail;
            this.tail.prev = n;
        } else {
            Node prevFirst = this.head.next;
            this.head.next = n;
            n.prev = this.head;
            n.next = prevFirst;
            prevFirst.prev = n;
        }
    }
    
    public Node removeLast(){
        Node last = this.tail.prev;
        last.prev.next = this.tail;
        this.tail.prev = last.prev;
        last.next = last.prev = null;
        return last;
    }
    
    public void remove(Node n){
        n.prev.next = n.next;
        n.next.prev = n.prev;
        n.next = n.prev = null;
    }
    
    public boolean isEmpty(){
        return this.head.next.isDummy;
    }
}

class LFUCache {    
    // Maps key to the corresponding node
    public HashMap<Integer,Node> nodes;
    
    // Maps used count to a DLL maintaining LRU ordering
    public HashMap<Integer,DLL> LRU;
    public int capacity;
    public int minCount;
    
    public LFUCache(int capacity) {
        this.capacity = capacity;
        this.nodes = new HashMap<>();
        this.LRU = new HashMap<>();
        this.minCount = -1;
    }
    
    public void addNode(Node n){
        if(!this.LRU.containsKey(n.count)){
            this.LRU.put(n.count, new DLL());
        }
        this.LRU.get(n.count).addFirst(n);
    }
    
    // Remove a node from its previous DLL, update count,
    // add to its new DLL
    public void updateNode(Node n){
        DLL currDLL = this.LRU.get(n.count);
        currDLL.remove(n);
        n.count += 1;
        this.addNode(n);
        
        // The node we are updating was the last node of the min freq, update it
        if(this.minCount == n.count - 1 && currDLL.isEmpty()){
            this.minCount = n.count;
        }
    }
    
    public int get(int key) {
        // Key does not map to an existing node
        if(!this.nodes.containsKey(key)){
            return -1;
        }
        Node currNode = this.nodes.get(key);
        this.updateNode(currNode);
        return currNode.val;
    }
    
    public void evict(){
        Node evictedNode = this.LRU.get(this.minCount).removeLast();
        this.nodes.remove(evictedNode.key);
    }
    
    public void put(int key, int value) {
        // Edge case
        if(this.capacity == 0){
            return;
        }
        
        // Add a node for the first time
        Node currNode;        
        if(!this.nodes.containsKey(key)){
            // Evict LFU node that is LRU
            if(this.nodes.size() == this.capacity){
                this.evict();
            }
            
            // Map the key to the newly created node
            currNode = new Node(key, value);
            currNode.count = this.minCount = 1;
            this.nodes.put(key, currNode);

            // Add the new node as MRU for freq count 1
            this.addNode(currNode);
        }
        else{
            currNode = this.nodes.get(key);
            currNode.val = value;
            this.updateNode(currNode);
        }
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */