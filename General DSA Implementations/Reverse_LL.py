class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        if self.next is not None:
            return "Node with value " + str(self.val) + " has next ptr to Node with value " + str(self.next.val)
        else:
            return "Node with value " + str(self.val) + " has next ptr to None"


def print_ll(head):
    current_node = head
    while current_node is not None:
        print(current_node)
        current_node = current_node.next 

def get_tail(head):
    current_node = head
    while current_node is not None:
        if current_node.next is None:           # The tail of the LL has been located, return it
            return current_node
        current_node = current_node.next


# O(n) Reverse a Linked List and return the new head of the list
def reverse_ll(head):
    tail = get_tail(head)                       # O(n) operation

    # Reverse LL in place O(n)
    prev = None
    current_node = head 
    while current_node is not None:
        nxt = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = nxt

    return tail # The new head of the LL


# Build Sample LL (1 -> 2 -> 3 -> 4 -> None)
four = ListNode(4)
three = ListNode(3, four)
two = ListNode(2, three)
one = ListNode(1, two)

# Print the LL, then reverse and print
head = one
print_ll(head)
print_ll(reverse_ll(head))


