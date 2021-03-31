# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        def sameTree(sCurr, tCurr):
            # Base case, both nodes are null
            if(not sCurr and not tCurr):
                return True
            # Base case, only one of the two nodes is null
            if(not sCurr or not tCurr):
                return False
            
            # Recurse left and right subtrees if value matches
            return sCurr.val == tCurr.val and sameTree(sCurr.left, tCurr.left) and sameTree(sCurr.right, tCurr.right)
            
        
        # Check each subtree that shares the same root as t
        q = deque()
        q.append(s)
        while q:
            curr = q.popleft()
            if(curr.val == t.val and sameTree(curr, t)):
                return True
            
            # Expand subtrees
            if(curr.left):
                q.append(curr.left)
            if(curr.right):
                q.append(curr.right)
        
        return False
         
        
