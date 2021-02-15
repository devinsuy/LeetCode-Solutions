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
    public TreeNode invertTreeUtil(TreeNode node){
        if(node == null) return null;
        else if(node.left == null && node.right == null)     // Node with no children is already inverted
            return node;
        
        // Recursively invert tree nodes
        TreeNode temp = node.left;
        node.left = invertTreeUtil(node.right);
        node.right = invertTreeUtil(temp);
        
        return node;
    }
    
    public TreeNode invertTree(TreeNode root) {
        return root == null ? null : invertTreeUtil(root);
    }
}