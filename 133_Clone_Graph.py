from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Edge case
        if(node is None): 
            return None
        
        maxId = float('-inf')
        visited = set([])
        adjIds = defaultdict(list)              # Map node id to list of its neighbor ids 
        st = [node]
        
        # BFS traversal of graph to build adjIds and determine maxId of the graph
        while st:
            curr = st.pop()
            if(curr.val in visited): continue
            if(curr.val > maxId): maxId = curr.val
            visited.add(curr.val)
            
            # Expand neighbors
            for adj in curr.neighbors:
                if(adj.val not in visited): st.append(adj)
                adjIds[curr.val].append(adj.val)
        
        # Clone graph, each node is stored at index 1 less than its ID
        nodes = [Node(i) for i in range(1, maxId+1)] 
        startNode = nodes[node.val-1]
        
        # Link each node to its neighbor nodes
        for nodeId, adjList in adjIds.items():
            curr = nodes[nodeId-1]
            for adjId in adjList:
                curr.neighbors.append(nodes[adjId-1])
        
        return startNode
        
        