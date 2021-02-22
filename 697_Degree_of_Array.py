'''
Input: VALID, non empty list of positive integers
Ouput: The smallest length of a subarray with deg(sub) == deg(nums)

Degree: let a = frequency map for nums, 
    degree = max(a.values())

Subarrays must be CONTIGUOUS unlike subsequences

We only care about numbers that have frequency == deg(nums)
    - There may be multiple numbers in nums that share the same frequency as deg(nums)


Collections:
- Iterate through nums, map value to list of indicies the value appears at
    - Freq(value) = len(indexMap[val])
    - deg(nums) = max(freq(value) for value in nums)
    
- topFreqNums = {}
    - topFreqNums only contains values who have freq(val) == deg(nums)
    - Maps value to the minimum subarray size needed to reach that frequency
        - The min subarray size is found by subtracting last appearance index by the first in indexMap
            -EX: freqMap[val][-1] - freqMap[val][0] + 1 since we iterate, they are built in sorted ascending
            
    - For left index, right index inclusive
        - Size of subarray is right-left + 1

- Return the min size in topFreqNums

Edge cases:
    - Input is validated
    - Singleton list nums: return 1
    - List of all same num: return len(nums)
    - List of all distinct nums: return 1
'''

from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Singleton list
        if(len(nums) == 1):
            return 1
        
        # Map each value to the indices it appears at, calculate deg(nums)
        indexMap = defaultdict(list)
        degNums = float('-inf')
        for i, val in enumerate(nums):
            indexMap[val].append(i)
            currFreq = len(indexMap[val]) 
            if(currFreq > degNums):
                degNums = currFreq
        
        # A degree of 1 can at minimum be reached by any singleton subarray
        if(degNums == 1):
            return 1
        
        # List only contains one distinct number
        # deg(nums) = min(deg(subarr)) = len(nums)
        if(len(indexMap) == 1):
            return len(nums)
        
        # For values (who have same freq as deg(num)) determine the min 
        # subarray size to obtain freq(val), track global minimum
        minLen = float('inf')
        for val, indices in indexMap.items():
            if(len(indices) == degNums):
                subarrLen = indices[-1] - indices[0] + 1
                if(subarrLen < minLen):
                    minLen = subarrLen
                
        return minLen
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        