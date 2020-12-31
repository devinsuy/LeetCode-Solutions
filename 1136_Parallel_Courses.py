from typing import List
from collections import deque

# References in nodes_in not utilized can be replaced 
# for integer in-degree for performance improvement

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        # Base case
        if N == 1: return 1
        
        # Build an adjacency list from the relations, 
        # index by node number 1 -> N 
        nodes_out = [None]
        nodes_in = [None]
        for i in range(N): nodes_out.append(set([]))
        for i in range(N): nodes_in.append(set([]))

        for relation in relations:
            src, dst = relation
            nodes_out[src].add(dst)
            nodes_in[dst].add(src) 
        
        # Classes taken on first term and last term
        start_nodes = set([])
        end_nodes = set([])
        
        # Starting nodes have no incoming edges
        # Ending nodes have no outgoing edges
        for i in range(1, N+1):
            if len(nodes_in[i]) == 0: start_nodes.add(i)
            if len(nodes_out[i]) == 0: end_nodes.add(i)

        # Graph is not a DAG if it has no leaf nodes
        if len(end_nodes) == 0:
            return -1

        q = deque(start_nodes)
        num_sems = 0

        while q: 
            # Each "semester" the queue empties out as classes that have
            # no outstanding pre-requeisites are taken
            num_sems += 1

            # Explore only nodes present at the start of the semester
            for _ in range(len(q)):
                curr_id = q.popleft()

                # For each neighbormark each as visited by the current node 
                # (pre-req class for neighbor has been taken)
                for adj_id in nodes_out[curr_id]:
                    nodes_in[adj_id].remove(curr_id)

                    # If all pre-req classes for neighbor fufilled, add to q
                    # to be taken next semester
                    if len(nodes_in[adj_id]) == 0:
                        q.append(adj_id)
        
        # If a course was left uncompleted (its pre-reqs unfifilled)
        for i in range(1, N+1):
            if len(nodes_in[i]) > 0:
                return -1

        # All courses were completed
        return num_sems        


# Expected: 2
N = 3
relations = [[1,3],[2,3]]


# Expected: -1
# Graph creates a cycle
N = 3
relations = [[1,2],[2,3],[3,1]]


# Starting nodes have outgoing edges but no incoming
# Ending nodes have incoming edges but no outgoing
N = 9
relations = [
    [1,5], [2,5], [3,6], [3,7], [4,7],
    [5,6], [5,8], [6,8], [7,8],
    [8,9], [7,9]
]

s = Solution()
print(s.minimumSemesters(N, relations))