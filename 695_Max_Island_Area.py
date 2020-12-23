from typing import List 

class Solution:
    # Given the indices of a particular cell, return a list of
    # (row, col) indice tuples of valid 4-directional neighbors
    def get_neighbors(self, row, col):
        neighbors = []
        if row-1 >= 0: neighbors.append((row-1, col))
        if row+1 < self.num_rows: neighbors.append((row+1, col))
        if col-1 >= 0: neighbors.append((row, col-1))
        if col+1 < self.num_cols: neighbors.append((row, col+1))
        
        return neighbors
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Maintain a list of visited cells 
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])
        self.visited = []
        for _ in range(self.num_rows): self.visited.append([False] * self.num_cols)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1 and not self.visited[i][j]:
                    self.visited[i][j] = True
        


arr = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
 ]

s = Solution()
print(s.maxAreaOfIsland(arr))

