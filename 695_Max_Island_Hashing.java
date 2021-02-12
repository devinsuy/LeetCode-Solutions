import java.util.Stack;

class Point{
    public int i;
    public int j;
    public Point(int i, int j){
        this.i = i;
        this.j = j;
    }
    public int hashCode(){
        return Objects.hash(this.i, this.j);
    }
    public boolean equals(Object obj){    
        return (this.i == ((Point) obj).i) && (this.j == ((Point) obj).j);
    }
}

class Solution {
    public HashSet<Point> visited;
    
    public int BFS(int[][] grid, Point p){
        Stack<Point> st = new Stack<Point>();
        Point curr, adj;
        int islandSize = 0;
        st.push(p);
        
        // BFS traversal of island
        while(!st.isEmpty()){
            curr = st.pop();
            if(this.visited.contains(curr)) continue;
            islandSize++;
            this.visited.add(curr);
            
            // Add each 4-directional neighbor if exists and unvisited
            if(curr.i-1 >= 0 && grid[curr.i-1][curr.j] == 1){
                adj = new Point(curr.i-1, curr.j);
                if(!this.visited.contains(adj)) st.push(adj);
            }
            if(curr.i+1 < grid.length && grid[curr.i+1][curr.j] == 1){
                adj = new Point(curr.i+1, curr.j);
                if(!this.visited.contains(adj)) st.push(adj);
            }
            if(curr.j-1 >= 0 && grid[curr.i][curr.j-1] == 1){
                adj = new Point(curr.i, curr.j-1);
                if(!this.visited.contains(adj)) st.push(adj);
            }
            if(curr.j+1 < grid[0].length && grid[curr.i][curr.j+1] == 1){
                adj = new Point(curr.i, curr.j+1);
                if(!this.visited.contains(adj)) st.push(adj);
            }
        }
        return islandSize;
    }
    
    public int maxAreaOfIsland(int[][] grid) {
        this.visited = new HashSet<>();
        Point currPoint;
        int maxSize = Integer.MIN_VALUE;
        int islandSize;
        
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                currPoint = new Point(i, j);
                
                // Traverse unvisited island, update size if larger
                if(grid[i][j] == 1 && (!visited.contains(currPoint))){
                    islandSize = this.BFS(grid, currPoint);
                    if(islandSize > maxSize) maxSize = islandSize;
                }
            }
        }        
        return maxSize == Integer.MIN_VALUE ? 0 : maxSize;
    }
}