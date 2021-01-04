import java.util.Queue;
import java.util.LinkedList;

class Solution {
    boolean[][] visited;
    int[][] grid;

    public int BFS(int[] node){
        Queue<int[]> q = new LinkedList<int[]>();
        q.add(node);
        boolean[] adj = new boolean[4];
        int[] curr_node;
        int[] adj_node;
        int i, j;
        int curr_size = 0;

        while(!q.isEmpty()){
            curr_node = q.remove();
            i = curr_node[0];
            j = curr_node[1];    
            curr_size++;

            // Determine valid neighbors
            adj[0] = (j-1 >= 0 && grid[i][j-1] == 1);
            adj[1] = (j+1 != grid[0].length && grid[i][j+1] == 1);
            adj[2] = (i+1 != grid.length && grid[i+1][j] == 1);
            adj[3] = (i-1 >= 0 && grid[i-1][j] == 1);
           
            // Add each valid unvisited neighbor to queue
            if(adj[0] && !visited[i][j-1]) { 
                adj_node = new int[] {i, j-1};
                this.visited[i][j-1] = true;
                q.add(adj_node);
            }
            if(adj[1] && !visited[i][j+1]) { 
                adj_node = new int[] {i, j+1};
                this.visited[i][j+1] = true;
                q.add(adj_node);
            }
            if(adj[2] && !visited[i+1][j]) { 
                adj_node = new int[] {i+1, j};
                this.visited[i+1][j] = true;
                q.add(adj_node);
            }
            if(adj[3] && !visited[i-1][j]) { 
                adj_node = new int[] {i-1, j};
                this.visited[i-1][j] = true;
                q.add(adj_node);
            }
        }
        
        return curr_size;
    }

    public int maxAreaOfIsland(int[][] grid) {
        int COL_LEN = grid.length;
        int ROW_LEN = grid[0].length;
        this.grid = grid;
        this.visited = new boolean[COL_LEN][ROW_LEN];

        // [left, right, up, down], corresponding to whether
        // or not the current node has a neighbor there 
        boolean [] adj = new boolean[4]; 
        
        // Perform BFS (nodes likely to be densely populated)
        int max_area = Integer.MIN_VALUE;
        int [] curr_node;
        int curr_area;

        for(int i = 0; i < COL_LEN; i++){
            for(int j = 0; j < ROW_LEN; j++){
                // Avoid unnecessarily expanding nodes
                if (grid[i][j] == 0 || visited[i][j]) { 
                    continue; 
                } 
                curr_node = new int[] {i, j};
                this.visited[i][j] = true;
                curr_area = BFS(curr_node);
                if (curr_area > max_area) { max_area = curr_area; }
            }
        }
        
        // No islands were found
        if (max_area == Integer.MIN_VALUE) { return 0; }

        // Otherwise return the max area found from BFS
        return max_area;
    }

    public static void main(String[] args){
        // Expected: 6
        // int[][] grid = {
        //     {0,0,1,0,0,0,0,1,0,0,0,0,0},
        //     {0,0,0,0,0,0,0,1,1,1,0,0,0},
        //     {0,1,1,0,1,0,0,0,0,0,0,0,0},
        //     {0,1,0,0,1,1,0,0,1,0,1,0,0},
        //     {0,1,0,0,1,1,0,0,1,1,1,0,0},
        //     {0,0,0,0,0,0,0,0,0,0,1,0,0},
        //     {0,0,0,0,0,0,0,1,1,1,0,0,0},
        //     {0,0,0,0,0,0,0,1,1,0,0,0,0}
        // };

        // Expected: 4
        int[][] grid = {
            {1,1,0,0,0},
            {1,1,0,0,0},
            {0,0,0,1,1},
            {0,0,0,1,1}
        };

        // Expected: 0
        // int[][] grid = {
        //     {0,0,0,0,0,0,0,0}
        // };

        Solution s = new Solution();
        System.out.println(s.maxAreaOfIsland(grid));

    }
}
