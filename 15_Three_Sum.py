from typing import List
from collections import defaultdict

class Solution:
    # Builds a tuple of the three numbers in ascending order 
    def get_tuple(self, num_one, num_two, complement): 
        return tuple(sorted((num_one, num_two, complement)))
    
    # Check whether a number occurs enough times to be used as a valid triplet
    def valid_triplet(self, num_one, num_two, complement):
        if complement not in self.num_counts:
            return False
        elif num_one == num_two:
            # All three numbers are the same value
            if num_one == complement:
                return not self.num_counts[num_one] < 3
            # Only two of the three numbers are the same
            else:
                return not self.num_counts[num_one] < 2
        # Two of the three numbers are the same
        elif (complement == num_one or complement == num_two): 
            return not self.num_counts[complement] < 2

        return True

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Base cases
        if len(nums) < 3: return []
        if len(set(nums)) == 1:
            if nums[0] == 0:
                return [[nums[0], nums[0], nums[0]]]
            else: return []

        # Map numbers to their frequency count
        nums.sort()
        self.num_counts = defaultdict(int)
        for num in nums: self.num_counts[num] += 1

        # Maintain triplets as a set of sorted tuples, 
        # no duplicates will be added
        triplets = set([])
        
        # Generate pairs, avoid generating unnecessary pairs
        for i in range(0, len(nums)):
            num_one = nums[i]
            if i > 0 and num_one == nums[i-1]: 
                continue
            
            # Pair with inner numbers
            for j in range(i+1, len(nums)):
                num_two = nums[j]
                if num_two > i+1 and num_two == nums[j-1]: 
                    continue
                complement = -1*(num_one + num_two)
        
                if self.valid_triplet(num_one, num_two, complement):
                    triplets.add(self.get_tuple(num_one, num_two, complement))
        
        return triplets


# Expected: [ [-1,-1,2], [-1,0,1] ]
# sorted: [-4,-1,-1,0,1,2]
a = [-1,0,1,2,-1,-4]


s = Solution()
print(s.threeSum(a))