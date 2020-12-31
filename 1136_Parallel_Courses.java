import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;

class Solution {
    public int minimumSemesters(int N, int[][] relations) {
        // Base case
        if (N == 1) { return 1; }

        // Initialize list of sets, where each index corresponds to the set of adj nodes
        ArrayList<HashSet<Integer>> node_out = new ArrayList<HashSet<Integer>>(N+1);
        node_out.add(null);
        for(int i = 0; i < N; i++){ node_out.add(new HashSet<Integer>()); }
        
        // Build adjacency list for each node, indexed by node_id
        int src, dst;
        int[] in_degree = new int[N+1];

        for(int[] rel : relations){
            src = rel[0];
            dst = rel[1];
            node_out.get(src).add(dst);
            in_degree[dst]++;
        }
        
        // Start nodes have in degree of 0
        // End nodes have out degree of 0
        ArrayList<Integer> start_nodes = new ArrayList<Integer>();
        ArrayList<Integer> end_nodes = new ArrayList<Integer>();

        for(int i = 1; i <= N; i++){
            if (in_degree[i] == 0) { start_nodes.add(i); }
            if (node_out.get(i).size() == 0) { end_nodes.add(i); } 
        }

        // A DAG must have an end node
        if (end_nodes.size() == 0){ return -1; }

        // Run topological sorting
        LinkedList<Integer> q = new LinkedList<Integer>(start_nodes);
        HashSet<Integer> curr_adj;
        int stop, curr_id, not_visited_size;
        int num_semesters = 0;

        // Continue while there are still valid classes
        while (!q.isEmpty()){
            num_semesters++;

            // Iterate through each "class" taken this semester
            stop = q.size();
            for(int i = 0; i < stop; i++){
                curr_id = q.removeFirst();
                curr_adj = node_out.get(curr_id);

                // For each class that the current class is pre-req,
                // fufill the pre-req, if all fufilled, add class to
                // queue to be taken next semester
                for(int adj_id : curr_adj){
                    not_visited_size = --in_degree[adj_id];
                    if (not_visited_size == 0) { q.addLast(adj_id); }
                }
            }
        }
        
        // Check if each class had its requirements fufilled
        // (implying that all classes were able to be taken)
        for (int num_remaining : in_degree){
            if(num_remaining > 0){ return -1; }
        }

        return num_semesters;
    }

    public static void main(String[] args){
        Solution s = new Solution();

        // Expected: 2
        // int N = 3;
        // int[][] relations = {{1,3},{2,3}};
        
        
        // Expected: -1
        // Graph creates a cycle
        // int N = 3;
        // int[][] relations = {{1,2},{2,3},{3,1}};
        
        // Expected: 5        
        // Starting nodes have outgoing edges but no incoming
        // Ending nodes have incoming edges but no outgoing
        int N = 9; 
        int[][] relations = {
            {1,5}, {2,5}, {3,6}, {3,7}, {4,7},
            {5,6}, {5,8}, {6,8}, {7,8},
            {8,9}, {7,9}
        };

        System.out.println(s.minimumSemesters(N, relations));
    }
}
