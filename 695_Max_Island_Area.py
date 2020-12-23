from typing import List 
from collections import deque

class Solution:
    # Given the indices of a particular cell, return a list of
    # (row, col) indice tuples of valid 4-directional neighbors
    def get_neighbors(self, row, col):
        neighbors = []
        if row-1 >= 0 and self.grid[row-1][col] == 1 and not self.visited[row-1][col]: 
            neighbors.append((row-1, col))
        if row+1 < self.num_rows and self.grid[row+1][col] == 1 and not self.visited[row+1][col]: 
            neighbors.append((row+1, col))
        if col-1 >= 0 and self.grid[row][col-1] == 1 and not self.visited[row][col-1]:
            neighbors.append((row, col-1))
        if col+1 < self.num_cols and self.grid[row][col+1] == 1 and not self.visited[row-1][col+1]:
            neighbors.append((row, col+1))
        
        return neighbors
    

    # Perform BFS from a given cell, return size 
    # of island once entirely explored
    def BFS(self, row, col):
        q = deque()
        q.append((row,col))
        island_size = 0

        # Explore each cell part of the island, mark as
        # visited, and incremend island_size
        while len(q) != 0:
            curr_row, curr_col = q.popleft()
            if self.visited[curr_row][curr_col]: 
                continue

            # Mark explored and continue exploration from neighbors
            self.visited[curr_row][curr_col] = True
            island_size += 1
            q.extend(self.get_neighbors(curr_row, curr_col))

        return island_size


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = float('-inf')

        # Maintain a list of visited cells 
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])
        self.grid = grid
        self.visited = []
        for _ in range(self.num_rows): self.visited.append([False] * self.num_cols)
        
        # Iterate through cells, call BFS on unvisited islands
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1 and not self.visited[i][j]:
                    island_size = self.BFS(i, j)
                    if island_size > self.max_area: 
                        self.max_area = island_size

        # No islands were found
        if self.max_area == float('-inf'): return 0
        else: 
            return self.max_area
        

# Expected: 6
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

# Expected: 0
arr = [[0,0,0,0,0,0,0,0]]

# Expected: 4
arr = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
]

s = Solution()
print(s.maxAreaOfIsland(arr))

