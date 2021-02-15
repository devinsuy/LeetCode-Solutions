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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // Edge cases
        if(p == null && q == null)
            return true;
        if(p == null && q != null)
            return false;
        if(p != null && q == null)
            return false;
        
        Queue<TreeNode> pQue = new LinkedList<>();
        Queue<TreeNode> qQue = new LinkedList<>();
        TreeNode pCurr, qCurr;
        pQue.add(p);
        qQue.add(q);
        
        // Perform Iterative BFS traversal
        while(!pQue.isEmpty()){
            if(pQue.size() != qQue.size())      // Both queues should have identical size if the same tree
                return false;
            pCurr = pQue.poll();
            qCurr = qQue.poll();
            
            // Each respective node from both trees should have the same value
            if(pCurr.val != qCurr.val)
                return false;
            
            // Expand children
            if(pCurr.left != null){
                if(qCurr.left == null) return false;
                pQue.add(pCurr.left);
            }
            if(pCurr.right != null){
                if(qCurr.right == null) return false;
                pQue.add(pCurr.right);
            }
            if(qCurr.left != null){
                if(pCurr.left == null) return false;
                qQue.add(qCurr.left);
            }
            if(qCurr.right != null){
                if(pCurr.right == null) return false;
                qQue.add(qCurr.right);
            }
        }
        
        // Second tree should be fully traversed same time as the first
        // trees are identical only if both queue emptied out at the same time
        return qQue.isEmpty();
    }
}