import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Edge case
        if(not intervals):
            return [newInterval]
        
        # Add the new interval into the sorted list O(n) 
        bisect.insort(intervals, newInterval)      
        
        merged = []
        prev = intervals[0]
        i = 1
        
        while(i < len(intervals)):
            curr = intervals[i]
            
            # Overlap found, merge until not possible
            if(prev[1] >= curr[0]):
                while(prev[1] >= curr[0]):
                    minStart = min(prev[0], curr[0])
                    maxEnd = max(prev[1], curr[1])
                    prev = [minStart, maxEnd]
                    i += 1
                    if(i >= len(intervals)): 
                        break
                    curr = intervals[i]
                
                # Append the newly created merged interval, followed by the remaining 
                # intervals (description states none of these will not be overlapping)
                merged.append(prev)
                merged.extend(intervals[i:])
                return merged
            
            # Otherwise there is no overlap here, append and update pointers
            merged.append(prev)
            prev = curr
            i += 1
        
        # The insert caused no overlap, all intervals checked, append the last element
        merged.append(prev)
        
        return merged