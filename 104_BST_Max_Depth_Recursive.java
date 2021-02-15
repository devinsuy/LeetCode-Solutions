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
    public int maxDepthUtil(TreeNode node, int depth){
        // Base case, leaf node reached
        if(node.left == null && node.right == null)
            return depth;
        
        // Otherwise recurse, depth at this node is the max of the left and right subtree depths
        int leftDepth, rightDepth;
        leftDepth = rightDepth = 0;
        if(node.left != null)
            leftDepth = maxDepthUtil(node.left, depth+1);
        if(node.right != null)
            rightDepth = maxDepthUtil(node.right, depth+1);
        
        return Math.max(leftDepth, rightDepth);
    }
    
    public int maxDepth(TreeNode root) {
        // Base cases
        if(root == null)
            return 0;
        if(root.left == null && root.right == null)
            return 1;
        
        return maxDepthUtil(root,  1);
    }
}