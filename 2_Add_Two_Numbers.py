# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Assign first node sum
        l1Ptr = l1
        l2Ptr = l2
        currSum = l1Ptr.val + l2Ptr.val
        currVal = currSum % 10
        hasCarry = currSum >= 10
        if hasCarry: carry = currSum // 10
        
        head = currNode = ListNode(currVal)
        l1Ptr = l1Ptr.next
        l2Ptr = l2Ptr.next
        
        while(l1Ptr is not None or l2Ptr is not None):
            # Assign value and advance pointer if end of list not reached
            # otherwise a null node from one list contributes 0 to the curr sum
            if(l1Ptr is not None): 
                leftVal = l1Ptr.val
                l1Ptr = l1Ptr.next
            else: 
                leftVal = 0 
            if(l2Ptr is not None): 
                rightVal = l2Ptr.val
                l2Ptr = l2Ptr.next
            else: 
                rightVal = 0
            
            # Calculate value of current node, adding previous carry if applicable
            currSum = leftVal + rightVal
            if(hasCarry): currSum += carry              
            currVal = currSum % 10
            
            # Assign carry for next node if relevant
            hasCarry = currSum >= 10
            if(hasCarry): carry = currSum // 10
            
            nextNode = ListNode(currVal)
            currNode.next = nextNode
            currNode = nextNode
        
        # Last node(s) contributed a carry sum past the end of the list, add it as the last node
        if(hasCarry):
            currNode.next = ListNode(carry)
        
        return head
            

        
        