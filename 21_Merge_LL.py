'''
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_LL(self, head):
        curr = head
        vals = []
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next 
        print(vals)
        return vals

    def get_min(self, node_1, node_2):
        if node_1 is None and node_2 is None: return (None, None, None)
        if node_1 is None: return (node_2, None, node_2.next)
        if node_2 is None: return (node_1, node_1.next, None)

        if node_1.val <= node_2.val: 
            return (node_1, node_1.next, node_2)
        else:
            return (node_2, node_1, node_2.next)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr_node, l_node, r_node = self.get_min(l1, l2)
        head = curr_node

        while True:
            next_node, l_node, r_node = self.get_min(l_node, r_node)
            if next_node is None: break
            curr_node.next = next_node
            curr_node = next_node
        
        return head
            
def create_LL(vals):
    curr_node = head = ListNode(vals[0])
    for val in vals[1:]:
        next_node = ListNode(val)
        curr_node.next = next_node
        curr_node = next_node
    
    return head


# Test Case: Expected [1,1,2,3,4,4]
l1 = create_LL([1,2,4])
l2 = create_LL([1,3,4])
s = Solution()
print(s.print_LL(s.mergeTwoLists(l1, l2)))
