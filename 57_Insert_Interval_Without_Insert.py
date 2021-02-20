import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Edge case
        if(not intervals):
            return [newInterval]
        
        # Use binary search to locate the index we would insert the new interval O(logn)
        insertIndex = bisect.bisect(intervals, newInterval)
        
        # The item belongs at the front of the list
        if(insertIndex == 0):
            i = 0
            prev = newInterval
            curr = intervals[i]
            merged = []
        # The item would be inserted somewhere past the front
        else:
            i = insertIndex - 1
            prev = intervals[i]
            curr = newInterval
        
        
        # Copy all intervals up to the element left of our insert (these are unaffected)
        merged = intervals[:i]
        
        # Check the remaining intervals for merging
        while(True):
            if(prev[1] >= curr[0]):                         # There is overlap between these intervals
                while(prev[1] >= curr[0]):
                    # Merge the two intervals
                    minStart = min(prev[0], curr[0])
                    maxEnd = max(prev[1], curr[1])
                    prev = [minStart, maxEnd]

                    # Update pointer, merging may not yet be done
                    i += 1
                    if(i == len(intervals)): break
                    curr = intervals[i]
                
                # Add the newly merged interval, copy the remaining intervals
                merged.append(prev)
                merged.extend(intervals[i:])
                return merged
            
            # There is no overlap, add interval and advance pointers
            else:
                merged.append(prev)
                i += 1
                
                # The end of the list has been reached, add the last element
                if(i == len(intervals)):
                    merged.append(curr)
                    return merged
                
                prev = curr
                curr = intervals[i]
                