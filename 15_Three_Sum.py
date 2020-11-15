from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Base case 
        if len(nums) <= 2:
            return []

        # Map each number to the amount of times it occurs
        num_counts = defaultdict(int)
        for num in nums: num_counts[num] += 1
        if len(num_counts) == 1 and len(nums) > 2:
            return [[nums[0], nums[0], nums[0]]]

        # Maintain a set of tuples, no duplicates 
        triplets = set([])
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num_1 = nums[i]
                num_2 = nums[j]
                complement = -1 * (num_1 + num_2)

                # No valid third number exists
                if complement not in num_counts: continue

                # For repeating values in the triplet, the value must occur
                # in the original list ATLEAST the amount of times in the triplet
                trip = [num_1, num_2, complement]
                trip_counts = defaultdict(int)
                for num in trip: 
                    trip_counts[num] += 1
                skip = False
                for num, count in trip_counts.items():
                    if num_counts[num] < count:
                        skip = True
                        break
                
                # Check the 6 possible permutations to avoid adding duplicate triplets
                if not skip:
                    check_set = [
                        (num_1, num_2, complement),
                        (num_1, complement, num_2),
                        (num_2, num_1, complement),
                        (num_2, complement, num_1),
                        (complement, num_1, num_2),
                        (complement, num_2, num_1)
                    ]
                    for trip in check_set:
                        if trip in triplets:
                            skip = True
                            break 
                    if not skip: triplets.add((num_1, num_2, complement))
        
        return triplets

a = [-1,0,1,2,-1,-4]
b = [0,0,0]
c = [1,2,-2,-1]
d = [-1,0,1,0]

s = Solution()
print(s.threeSum(a))