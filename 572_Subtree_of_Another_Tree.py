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
            # Base case, single node
            if(not sCurr.left and not sCurr.right):
                if(tCurr.left or tCurr.right):
                    return False
                return sCurr.val == tCurr.val
            
            # Both nodes should have a left or right subtree if the other does
            if(sCurr.left and not tCurr.left): return False
            if(not sCurr.left and tCurr.left): return False
            if(tCurr.right and not sCurr.right): return False
            if(not tCurr.right and sCurr.right): return False
            
            # Both nodes should have equivalent children, recurse subtrees
            if(not tCurr.left and not tCurr.right):   
                return sCurr.val == tCurr.val
            else:
                leftMatches = rightMatches = True
                if(tCurr.left):
                    if(not sCurr.left or sCurr.left.val != tCurr.left.val):
                        return False
                    else:
                        leftMatches = sameTree(sCurr.left, tCurr.left)

                if(tCurr.right):
                    if(not sCurr.right or sCurr.right.val != tCurr.right.val):
                        return False
                    else:
                        rightMatches = sameTree(sCurr.right, tCurr.right)
            
            return leftMatches and rightMatches
        
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
         
        
