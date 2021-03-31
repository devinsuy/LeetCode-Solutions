from collections import deque

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        N = len(isConnected)
        
        # Edge case
        if(N == 1):
            return 1
        
        visited = set([])
        numProvinces = 0
        
        for i in range(N):
            if(i in visited):
                continue
            st = deque([i])
            numProvinces += 1
            
            # BFS traversal
            while st:
                curr = st.pop()
                if(curr in visited): 
                    continue
                visited.add(curr)
                adjList = isConnected[curr]
                
                # Expand neighbors
                for adj in range(N):
                    if(adjList[adj] == 1):
                        st.append(adj)
        
        return numProvinces
                
                