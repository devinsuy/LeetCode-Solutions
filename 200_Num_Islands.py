"""
Input: 2D array of "cells" marked
   "1" : land
   "0" : water, anything outside of indices is also considered water
Output: The number of islands in the grid

Assumptions:
    - An "island" can be a single isolated landmass, OR connected landmasses
        - So long as the perimeter landmass is surrounded by water cells on all 4 sides
    - Starting from a land cell, we can use BFS to visit all neighbor land cells
    - The number of times we call BFS = the number of islands
    - A valid adjacent neighbor (row, column) is one whose indicies remain in bounds
        - and differ by at most 1 axis by a value of 1

Proceedure O(row*column) or "linear" time and memory:
    - Maintain a visited set that contains (row, column) tuples of cells we've checked
    - Build get_neighbors function that returns valid neighbors of a cell [(row, column)] list
    - Iterate through all cells, if not visited AND grid[row][column] == 1, call BFS(row, column), increment island_count
        - Within BFS, pop from stack, call get_neighbors(current_row, current_column)
        - For each neighbor add to visited set, THEN if grid[neighbor_row][neighbor_column] == 1 -> push onto stack
    - Finish iteration, return island_count 

"""


class Solution:
    def __init__(self):
        self.visited = set([])   # Stores tuples (row, column) of cells that have been visited
        self.island_count = 0

    # Given a (row, column) tuple, and the grid
    # Returns a list of (row, column) tuples of valid neighbors
    def get_neighbors(self, indices, grid):
        neighbors = []
        row, column = indices
        
        if row - 1 >= 0:
            neighbors.append((row-1, column))
        if row + 1 < len(grid):
            neighbors.append((row+1, column))
        if column - 1 >= 0:
            neighbors.append((row, column-1))
        if column + 1 < len(grid[0]):
            neighbors.append((row, column+1))

        return neighbors

    def BFS(self, start_indices, grid):
        stack = [start_indices]

        while stack:
            current_indices = stack.pop()
            self.visited.add(current_indices)
            
            for neighbor in self.get_neighbors(current_indices, grid):        # Consider all valid adjacent neighbor cells
                # Continue BFS to mark "land" parts of the island
                if neighbor not in self.visited and grid[neighbor[0]][neighbor[1]] == "1":
                    self.visited.add(neighbor)
                    stack.append(neighbor)          
            
    def numIslands(self, grid) -> int:
        if grid is None or len(grid) == 0:          # Validation cases
            return 0

        # Linear pass through each cell
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1" and (row, column) not in self.visited:
                    self.island_count += 1
                    self.BFS((row, column), grid)   # Mark all parts of the discovered "island" as visited to avoid double counting
        
        return self.island_count




grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]   # Expected: 3

s = Solution()
print(s.numIslands(grid))