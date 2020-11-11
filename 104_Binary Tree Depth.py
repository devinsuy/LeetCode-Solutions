# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:        
        if root == None:
            return 0
        else:
            maxDepth = 1
        
        # Queue stores depth of the node followed by the node itself (FILO)
        queue = []
        queue.append(1)
        queue.append(root)
        
        while queue:
            currentNode = queue.pop()
            currentDepth = queue.pop()
            
            if currentDepth > maxDepth:
                maxDepth = currentDepth
            
            if currentNode.right != None:
                queue.append(currentDepth + 1)
                queue.append(currentNode.right)
            if currentNode.left != None:
                queue.append(currentDepth + 1)
                queue.append(currentNode.left)   
        
        return maxDepth