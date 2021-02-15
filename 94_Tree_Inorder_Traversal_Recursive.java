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
    public void inorderUtil(List<Integer> order, TreeNode node){
        boolean hasLeft = node.left != null;
        boolean hasRight = node.right != null;
        // Base case, leaf node reached
        if(!hasLeft && !hasRight){
            order.add(node.val);
            return;
        }
        
        // Traverse left subtree, add root, traverse right
        if(hasLeft)
            inorderUtil(order, node.left);
        order.add(node.val);
        if(hasRight)
            inorderUtil(order, node.right);            
    }
    
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> order = new ArrayList<>();
        if(root == null) return order;
        inorderUtil(order, root);
        return order;
    }
}