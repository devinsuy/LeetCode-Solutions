/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {    
    public int maxDepth(TreeNode root) {
        // Base cases
        if(root == null)
            return 0;

        // Maintain two stacks in line with one another
        Stack<TreeNode> nodes = new Stack<>();
        Stack<Integer> depths = new Stack<>();
        nodes.add(root);
        depths.add(1);
        
        TreeNode currNode;
        int currDepth;
        int maxDepth = 1;
        
        // Perform iterative DFS traversal of the tree
        while(!nodes.isEmpty()){
            currNode = nodes.pop();
            currDepth = depths.pop();
            
            if(currDepth > maxDepth)
                maxDepth = currDepth;
            
            // Expand each valid child node
            if(currNode.left != null){
                nodes.add(currNode.left);
                depths.add(currDepth + 1);
            }
            if(currNode.right != null){
                nodes.add(currNode.right);
                depths.add(currDepth + 1);
            }
        }
        return maxDepth;
    }
}