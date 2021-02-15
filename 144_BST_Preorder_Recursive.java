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

// Preorder Traversal [root, left, right] is the same ordering as DFS
class Solution {
    public TreeNode preorderUtil(List<Integer> output, TreeNode node){
        // Base cases
        if(node == null) return null;
        if(node.left == null && node.right == null)         // Leaf node reached
            return node;
        
        // Traverse root, left, right
        output.add(node.val);
        TreeNode left = preorderUtil(output, node.left);
        if(left != null)
            output.add(left.val);
        TreeNode right = preorderUtil(output, node.right);
        if(right != null)
            output.add(right.val);     
        
        // Root is traversed before left and right subtrees, it shouldn't return anything after
        return null;
    }
    
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> output = new ArrayList<Integer>();
        // Base cases, empty tree or singleton tree
        if(root == null)
            return output;
        if(root.left == null && root.right == null){
            output.add(root.val);
            return output;
        } 
        this.preorderUtil(output, root);
        
        return output;
    }
}