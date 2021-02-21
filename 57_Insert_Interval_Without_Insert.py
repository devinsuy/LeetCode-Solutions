import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Edge case
        if(not intervals):
            return [newInterval]
        
        # Locate index of where newInterval would be inserted using binary search O(logn)
        insertIndex = bisect.bisect(intervals, newInterval)
        
        prev = newInterval
        if(insertIndex == 0):
            merged = []
            i = 0
        else:
            i = insertIndex
            # Copy all elements up to one before the insertion
            merged = intervals[:i-1]
            
            # Check if the element just before the insertion point can be merged with newInterval
            intBeforeMerge = intervals[i-1]
            if(intBeforeMerge[1] >= newInterval[0]):
                prev = [min(intBeforeMerge[0], newInterval[0]), max(intBeforeMerge[1], newInterval[1])]
            else:
                merged.append(intBeforeMerge)
        
        # Merge until no longer possible, add the newly created interval
        while(i < len(intervals)):
            curr = intervals[i]
            if(prev[1] >= curr[0]):
                prev = [min(prev[0], curr[0]), max(prev[1], curr[1])]
                i += 1
            else: 
                break
        merged.append(prev)
        
        # Copy the remaining elements
        merged.extend(intervals[i:])
        return merged