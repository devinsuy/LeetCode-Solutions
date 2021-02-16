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
    // Approach #1 using visited set
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> order = new ArrayList<Integer>();
        if(root == null)
            return order;
        
        Stack<TreeNode> st = new Stack<>();
        st.add(root);
        HashSet<TreeNode> visited = new HashSet<>();
        TreeNode curr;
        
        while(!st.isEmpty()){
            curr = st.pop();
            if(!visited.contains(curr))
                visited.add(curr);
            
            // Fully visit left subtree before adding the current node
            if(curr.left != null && !visited.contains(curr.left)){
                st.add(curr);               // Re-add the current node in the stack below the left node
                st.add(curr.left);
            }
            else{
                order.add(curr.val);        // Left subtree visited, add current node and explore right
                if(curr.right != null)
                    st.add(curr.right);
            }
        }
        
        return order;
    }

    // Approach #2 inspried by medium article
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> order = new ArrayList<>();
        if(root == null)
            return order;
        Stack<TreeNode> st = new Stack<>();
        TreeNode curr = root;
        
        while(true){
            // Add all left nodes, ending at the bottom left subtree
            while(curr != null){
                st.add(curr);
                curr = curr.left;
            }
            // Exit condition, all nodes processed
            if(st.isEmpty())
                return order;
            // Left, root, then attempt to go as far left in the right subtree, repeat
            curr = st.pop();
            order.add(curr.val);
            curr = curr.right;
        }
    }
}