from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Define dimensions of matrix
        M = len(matrix)
        N = len(matrix[0])
        NUM_ELEMS = M*N
        
        # Base case, matrix only contains 1 row, traverse left to right
        if M == 1:
            return matrix[0]

        # O(M*N) auxillary memory, maintain visited matrix 
        visited = [[False] * N for _ in range(M) ]
        output = [None] * NUM_ELEMS
        output_ptr = 0

        ''' Notation: 
                right -> down -> left -> up -> right -> ...
                where direction = 
                    right: 0, down: 1, left: 2, up: 3
        '''
        direction = 0
        curr_i = 0
        curr_j = -1

        while output_ptr != NUM_ELEMS:
            # True when no previously visited cells hit
            completed = True

            # Current segment will traverse from init or up to right
            if direction == 0:    
                curr_j += 1
                for j in range(curr_j, N):
                    # Segment completed
                    if visited[curr_i][j]:
                        curr_j = j - 1
                        completed = False
                        break                    
                    visited[curr_i][j] = True
                    output[output_ptr] = matrix[curr_i][j]
                    output_ptr += 1
                if completed:
                    curr_j = N-1
                
            # Segment will traverse right to down
            elif direction == 1:
                curr_i += 1
                for i in range(curr_i, M):
                    if visited[i][curr_j]:
                        curr_i = i - 1
                        completed = False
                        break
                    visited[i][curr_j] = True
                    output[output_ptr] = matrix[i][curr_j]
                    output_ptr += 1
                if completed:
                    curr_i = M-1
                
            # Segment will traverse down to left 
            elif direction == 2:
                curr_j -= 1
                for j in range(curr_j, -1, -1):
                    if visited[curr_i][j]:
                        curr_j = j + 1
                        completed = False
                        break
                    visited[curr_i][j] = True
                    output[output_ptr] = matrix[curr_i][j]
                    output_ptr += 1
                if completed:
                    curr_j = 0

            # Segment will traverse left to up
            elif direction == 3:
                curr_i -= 1
                for i in range(curr_i, -1, -1):
                    if visited[i][curr_j]:
                        curr_i = i + 1
                        completed = False
                        break
                    visited[i][curr_j] = True
                    output[output_ptr] = matrix[i][curr_j]
                    output_ptr += 1
                if completed:
                    curr_i = 0
            
            # Update direction for next segment 
            next_direction = direction + 1
            if next_direction > 3:
                direction = 0
            else:
                direction = next_direction

        return output


# Expected: [1,2,3,6,9,8,7,4,5]
matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Expected: [1,2,3,4,8,12,11,10,9,5,6,7]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]


s = Solution()
print(s.spiralOrder(matrix))
