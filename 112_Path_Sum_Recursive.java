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
    public boolean pathSumUtil(TreeNode node, int targetSum, int currSum){
        int nextSum = currSum + node.val;
        boolean hasLeft = node.left != null;
        boolean hasRight = node.right != null;
        
        // Leaf node reached, check the sum
        if(!hasLeft && !hasRight)    
            return nextSum == targetSum;
        
        // Recurse to root node in both left and right tree, tracking running sum
        boolean sumExists = false;
        if(hasLeft)
            sumExists = pathSumUtil(node.left, targetSum, nextSum);
        if(!sumExists && hasRight)
            sumExists = pathSumUtil(node.right, targetSum, nextSum);
        
        return sumExists;
    }
    
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null)
            return false;
        
        return pathSumUtil(root, targetSum, 0);
    }
}