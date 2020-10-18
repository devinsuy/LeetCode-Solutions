# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time and memory
    def serialize_tree(self, root: TreeNode):      
        q = [root]                      # Use a FIFO structure to perform top down level order traversal
        serialized_tree = []

        while q:
            current_node = q.pop(0)
            serialized_tree.append(current_node.val)

            if current_node is None:    # A null node has no children
                continue

            if current_node.left is not None:
                q.append(current_node.left)
            if current_node.right is not None:
                q.append(current_node.right)
            
        return serialized_tree
            

    # O(n) time
    # def levelOrderBottom(self, root: TreeNode):
    #     if root == None:
    #         return []
    #     elif root.left == None and root.right == None:
    #         return [root]

    #     if type(root == TreeNode):
    #         tree_arr = self.serialize_tree(root)
    #     else:
    #         tree_arr = root

    #     # Map depth -> [start, end] indices that correspond to the nodes in the BST arr
    #     depth_indices = {}

    #     # Determine the max depth of the given tree
    #     # A full binary tree with depth d has exactly (2^d)-1 nodes
    #     max_depth = 0
    #     while 2 ** max_depth < len(tree_arr):
    #         max_depth += 1

    #     for depth in range(1, max_depth+1):
    #         end_index = (2 ** depth) - 2
    #         start_index = end_index // 2
    #         depth_indices[depth] = [start_index, end_index] 
        
    #     # We have a non-full binary tree
    #     if 2 ** max_depth - 1 != len(tree_arr):
    #         prev_depth_end = depth_indices[max_depth-1][1]
    #         depth_indices[max_depth] = [prev_depth_end + 1, len(tree_arr) - 1]

        
    #     # Starting from max depth, traverse left to right using the indices
    #     level_traversal = []
    #     for current_depth in range(max_depth, 0, -1):                  # Big-Theta(depth), entire traversal is still linear, accessing exactly n elements where n is # of nodes in tree
    #         start_index, end_index = depth_indices[current_depth]
    #         current_traversal = []
            
    #         for i in range(start_index, end_index + 1, 1):              # Big-Theta(2^depth)
    #             current_traversal.append(tree_arr[i])
    #         level_traversal.append(current_traversal)
        
    #     return level_traversal


    def levelOrderBottom(self, root : TreeNode):
        # Base Cases
        if root is None:
            return []

        # Map depth -> list of NODES at that level
        depth_nodes = {1 : [root]}
        max_depth = 1
        current_depth = 2

        while True:
            current_nodes = []                          # Build a list of nodes at this depth
            
            # Iterate through each node of the previous depth, appending left
            # then right children of each (which are the nodes at this depth) 
            for node in depth_nodes[current_depth - 1]:
                if node is not None:
                    current_nodes.append(node.left)
                    current_nodes.append(node.right)
            
            # There are no new nodes at our current_depth, we are done
            if current_nodes == [None] * len(current_nodes):
                break
            
            # Our list ends with an unnecessary null node, trim it off 
            if current_nodes[-1] == None:
                current_nodes = current_nodes[:-1]

            depth_nodes[current_depth] = current_nodes
            current_depth += 1
            max_depth += 1
        
        traversal = []                                  # Build our traversal list from leaf nodes up to the root
        for depth in range(max_depth, 0, -1):           # Big-Theta(max_depth) 
            depth_values = []                           # We want to return the values at each depth, not the nodes
            for node in depth_nodes[depth]:             # O(2^depth)
                if node is not None:
                    depth_values.append(node.val)

            traversal.append(depth_values)
        
        return traversal
        
        


s = Solution()
print(s.levelOrderBottom([1]))


        

