import java.util.Stack;
import java.util.HashSet;
import java.util.ArrayList;
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
    public static int maxDepth(Integer[] nums) {
        // Base case
        if(nums.length == 1)
            return 1;
        
        int currDepth, nodeIndex, leftIndex, rightIndex;
        boolean[] visited = new boolean[nums.length];
        Stack<Integer> st = new Stack<>();
        st.add(0);
        int maxDepth = 1;
        
        // Use FIFO stack for iterative DFS 
        while(!st.isEmpty()){
            nodeIndex = st.pop();
            if(visited[nodeIndex])
                continue;
            visited[nodeIndex] = true;
            
            // The curr depth of the tree is the number of nodes
            // seen on the stack + the node just removed
            currDepth = 1 + st.size();
            if(currDepth > maxDepth)
                maxDepth = currDepth;
            
            // DFS traversal of children nodes
            leftIndex = 2*nodeIndex + 1;
            if(leftIndex < nums.length && !visited[leftIndex])
                st.add(leftIndex);
            rightIndex = leftIndex + 1;
            if(rightIndex < nums.length && !visited[rightIndex])
                st.add(rightIndex);
        }
        return maxDepth;
    }

    public static void main(String[] args){
        int b = 4;
        ArrayList<Integer> a = new ArrayList<>(b);
        System.out.println(a.get(0));
    }
}