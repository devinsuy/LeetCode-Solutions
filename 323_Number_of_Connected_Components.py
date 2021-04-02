from collections import deque

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Base cases
        if(n == 1):
            return 1
        
        # Map each node to a DLL of its neighbors
        nodeNeighbors = {}
        for i in range(n): nodeNeighbors[i] = deque()
        for edge in edges:
            node1, node2 = edge
            nodeNeighbors[node1].append(node2)
            nodeNeighbors[node2].append(node1)
        
        # Count each component by visiting each node
        visited = set([])
        componentCount = 0
        for nodeID in range(n):
            if(nodeID in visited):
                continue
                
            # Perform BFS traversal to expand the component
            q = deque([nodeID])
            while q:
                curr = q.popleft()
                if(curr in visited):
                    continue
                visited.add(curr)
                
                # Expand neighbors of the node
                for adjID in nodeNeighbors[curr]:
                    q.append(adjID)
            componentCount += 1
            
        return componentCount
        
            