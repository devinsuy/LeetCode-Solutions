from typing import List
import heapq

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Generate intervals of coverage [start, stop(exclusive)] from [0, n]
        intervals = []
        for i, tap in enumerate(ranges):
            if(i-tap < 0): leftBound = 0
            else: leftBound = i-tap
            if(i+tap > n): rightBound = n
            else: rightBound = i+tap
                
            # Avoid processing taps with 0 coverage
            if(leftBound != rightBound):
                intervals.append([leftBound, rightBound])
        
        # Sort intervals by left coverage O(nlogn)
        intervals.sort(key=lambda x: x[0])
        minNeeded = numTaps = leftIndex = 0
        
        while(True):
            # Base case, full coverage reached
            if(minNeeded >= n):
                return numTaps
            
            # For each interval covering left as much as we need, track the 
            # furthest right the interval covers 
            right = float('-inf')
            for i in range(leftIndex, len(intervals)):
                interval = intervals[i]
                
                # Update left index, next search will exclude all values to left (since sorted)
                if(interval[0] <= minNeeded and interval[1] > right):
                    right = interval[1]
                    leftIndex = i+1
            
            # If the left value was not covered there is a gap, not possible to cover all
            if(right == float('-inf')):
                return -1
            else: 
                numTaps += 1
                minNeeded = right
            
        
        
                
 

        