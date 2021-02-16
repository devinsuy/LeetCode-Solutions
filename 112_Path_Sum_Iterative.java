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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null)
            return false;
        
        // Maintain running sum and references to nodes
        Stack<TreeNode> st = new Stack<>();
        Stack<Integer> sum = new Stack<>();
        st.push(root);
        sum.push(0);
        
        boolean hasLeft, hasRight;
        TreeNode curr;
        int currSum;
        
        // Perform DFS tree traversal
        while(!st.isEmpty()){
            curr = st.pop();
            currSum = sum.pop() + curr.val;
            hasLeft = curr.left != null;
            hasRight = curr.right != null;
            
            // Leaf node reached
            if(!hasLeft && !hasRight){
                if(currSum == targetSum)        // Terminate upon finding sum
                    return true;
                continue;
            }
            
            // Expand children nodes
            if(hasLeft){
                st.push(curr.left);
                sum.push(currSum);
            } 
            if(hasRight){
                st.push(curr.right);
                sum.push(currSum);
            }
        }
        return false;
    }
}