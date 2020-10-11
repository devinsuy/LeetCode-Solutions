# LEVEL ORDER TRAVERSAL IS BFS ON A BST
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return "Node with value " + str(self.val)

def level_traversal(root):
    stack = [root]
    
    while stack:                            # Continue traversing until we have traversed the entire tree level by level 
        current_node = stack.pop(0)         # Use a FIFO convention
        print(current_node)

        # Add in children of the current node if there are any
        if current_node.left is not None:
            stack.append(current_node.left)
        if current_node.right is not None:
            stack.append(current_node.right)


# Leaf Nodes
two = Node(2)
four = Node(4)
five = Node(5)
seven = Node(7)

# Level 1 Nodes
three = Node(3, two, four)
six = Node(6, five, seven)

# Call the function
root = Node(5, three, six)
level_traversal(root)
