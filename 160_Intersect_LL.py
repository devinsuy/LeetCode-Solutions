'''
Input: the heads of two SLL
Output: A reference to the node the first node they share in common

- Hash each list node into a seen set
- Pointer to each SLL, on each pass advance to next node if has node
- Add node to set
- If current node already in set, return current node


- If a and b are the same length, they arrive at the intersection node at the same time

- Traverse both lists first to determine their lengths
- For the longer list, begin the currPtr len(longer) - len(shorter) nodes ahead of the other
- They will now reach the intersection at the same time
    - If they don't they have no intersection


Cases:
    - Lists are same length: reach intersection at same time (check if leftNode == rightNode -> return leftNode)
    - One list is longer than the other (shorter list may reach tail, stop once null)
        - Eventually the longer one will reach the intersection node, see it in seen, return the node
    - One list is only a single node long (same thing)
    - Both LL make it to null, return null (no intersection)
    
    
Constraints:
    - Time O(n), space O(1)
    - LL contains no cycles
    - Cannot modify LL
    
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Edge case, if either list is empty no intersection
        if(not headA or not headB):
            return None
        
        # Determine the lengths of each list O(L1 + L2)
        currA = headA
        currB = headB
        aLen = bLen = 0
        while(currA):
            aLen += 1
            currA = currA.next
        while(currB):
            bLen += 1
            currB = currB.next 
            
        # Advance the pointer of the longer list by their difference
        currA = headA
        currB = headB
        lenDiff = abs(aLen-bLen)
        if(aLen > bLen):
            for _ in range(lenDiff):
                currA = currA.next
        elif(bLen > aLen):
            for _ in range(lenDiff):
                currB = currB.next
                
        # A and B are the same length now and should arrive at the
        # intersection at the same time if one exists O(L1 + L2)
        while(currA and currB):
            if(currA == currB):
                return currA
            currA = currA.next
            currB = currB.next
                           
        # If either list is fully traversed without finding an intersection there is none
        return None
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        