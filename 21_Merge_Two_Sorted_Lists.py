# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Empty list, return the other
        if(not l1):
            return l2
        if(not l2):
            return l1
        
        # Assign the first node of the merged list as the greater of the two heads
        leftCurr = l1
        rightCurr = l2
        if(l1.val < l2.val):
            head = leftCurr
            leftCurr = leftCurr.next
        else:
            head = rightCurr
            rightCurr = rightCurr.next
        outputCurr = head
            
        # Merge output lists until both pointers reach end of their lists
        while leftCurr or rightCurr:
            # Both lists arent empty yet, compare
            if(leftCurr and rightCurr):         
                if(leftCurr.val < rightCurr.val):
                    outputCurr.next = leftCurr
                    leftCurr = leftCurr.next
                else:
                    outputCurr.next = rightCurr
                    rightCurr = rightCurr.next
            
            # Only the left list is non empty, link its next node
            elif(leftCurr):
                outputCurr.next = leftCurr
                leftCurr = leftCurr.next
            
            # Only the right list is nonempty, link its next node
            elif(rightCurr):
                outputCurr.next = rightCurr
                rightCurr = rightCurr.next
            
            outputCurr = outputCurr.next
        
        return head
                
            