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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> output = new ArrayList<Integer>();
        // Base case, empty tree
        if(root == null)
            return output;
        
        Stack<TreeNode> st = new Stack();
        st.add(root);
        TreeNode curr;
        
        // Stack is LIFO structure, add right children first then left,
        // LIFO will pop off left then right giving us [root,left,right]
        while(!st.isEmpty()){
            curr = st.pop();
            output.add(curr.val);
            if(curr.right != null)
                st.add(curr.right);
            if(curr.left != null)
                st.add(curr.left);
        }
        
        return output;
    }
}