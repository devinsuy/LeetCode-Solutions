from collections import defaultdict
import heapq

# Time Complexity: O(k*logn)
# Sapce Complexity: O(s)    where s = # distinct numbers            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Edge cases
        if(not nums):
            return []
        if(len(nums) < 2):
            return nums
        
        # Map each number to its frequency count O(n)
        numCounts = defaultdict(int)
        for num in nums:
            numCounts[num] += 1
        
        # Build a max heap O(n)
        maxHeap = []
        for num, freq in numCounts.items():
            heapq.heappush(maxHeap, (-freq, num))           # Negate frequency to convert to max heap
        
        # Build output O(k * logn)
        kMostFreq = []
        for _ in range(k):
            kMostFreq.append(heapq.heappop(maxHeap)[1])
        
        return kMostFreq
        
        