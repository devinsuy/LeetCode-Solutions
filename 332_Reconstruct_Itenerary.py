'''
Input: 2D List of src, dst IATA codes
Output: List of IATA codes in order of traversal starting from JFK

DFS traversal beginning from JFK
    - If there are multiple edges than can be taken, take them in lexical order


- Map ticket [src, dst] -> to the index in tickets it appears at
- Maintain a seen set([]) that contains the indices of tickets used for DFS
- Build output alongside DFS traversal

- Iterate through tickets, map src IATA to list of dst IATAs
    - Sort each list so that they are traversed in lexical order

'''

from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Edge cases
        if(not tickets):
            return []
        if(len(tickets) < 2):
            return tickets[0]
        
        # Map each src to a list of tuples containing the ticket  
        # index and the destination, sort in lexical order of dst
        srcDst = defaultdict(list)
        ticketIndex = {}
        for i, ticket in enumerate(tickets):
            srcDst[ticket[0]].append((ticket[1], i))
        for src in srcDst:
            srcDst[src].sort()
            
        visited = set([])
        output = []
        stIndices = []
        
        # DFS returns true if all tickets used, false otherwise
        def dfs(src: str):
            output.append(src)
            
            for indexDst in srcDst[src]:
                dst, ticketIndex = indexDst
                if(ticketIndex in visited):
                    continue
                stIndices.append(ticketIndex)
                visited.add(ticketIndex)
                if(dfs(dst)):
                    return True
                
                # DFS failed to reach end on current path, backtrack
                else:
                    visited.remove(ticketIndex)
                    stIndices.pop()
                    output.pop()
                    
            if(len(output) < len(tickets) + 1):
                return False
            else:
                return True
                
        # Begin traversal from JFK
        dfs("JFK")
        return output
        