'''
Difficulty of day: The max difficult of all the jobs assigned to that day
Difficulty of schedule: sum of each days difficulty

Constraints:
    - Atleast 1 task per day
    - task[i] requires task[i-1] to have been assigned previously (or on previous day)

- Enumerate all possible task schedules
- Check difficult of schedule, track min difficulty
- Optimize with memoization
    
Input: Array of integers reperesenting task difficulties
Output: Min difficulty (difficulty of the best schedule)

'''
class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        N = len(jobDifficulty)

        # Edge cases:
        # There is only one day assigned all tasks
        if(d == 1): return max(jobDifficulty)
        
        # There must be atleast one task per day, no schedule exits
        if(N < d): return -1
        
        # The only possible schedule is exactly one task per day
        if(N == d): return sum(jobDifficulty)        
        
        # DP map (sartIndex, remainDays) param tuples -> difficulty
        cache = {}
        
        def getDifficulty(startIndex: int, remainDays: int) -> int:
            paramTuple = (startIndex, remainDays)
            if(paramTuple in cache):
                return cache[paramTuple]
            
            # Base case, all remaining tasks are assigned to this last day
            if(remainDays == 1):
                currDayDiff = -1
                for i in range(startIndex, N):
                    currDayDiff = max(currDayDiff, jobDifficulty[i])
                cache[paramTuple] = currDayDiff
                return currDayDiff
            
            # Consider all partitions for the current day that allow
            # the following days to still be nonempty (keep atleast 1 task per day)
            minDayDiff = float('inf')
            currDayDiff = 0
            for i in range(startIndex, N - remainDays + 1):
                # Update the difficulty of the current partition to consider the next element
                currDayDiff = max(currDayDiff, jobDifficulty[i])
                
                # Calculate the total difficulty as that of the current partition 
                # and the difficulty of the remaining elements to be partitioned, track the min
                minDayDiff = min(minDayDiff, currDayDiff + getDifficulty(i+1, remainDays-1))
            
            cache[paramTuple] = minDayDiff
            return minDayDiff
        
        # Enumerate all possible task schedules, return the minimum difficulty
        return getDifficulty(0, d)
            
        
        
        
        
        
        