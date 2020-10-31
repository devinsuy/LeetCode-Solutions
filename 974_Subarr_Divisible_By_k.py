from typing import List
from collections import defaultdict

class Solution:
    # Each modulo value that appears MORE than once contributes 
    # [count*count-1] / 2 subarrays divisible by K, since the subarray
    # between any two indices that reach the same modluo value MUST be divisible by K
    # simply count the number of distinct (i,j) combinations aka (i,j) = (j,i)
    def get_sub_count(self, num_occurrences: int) -> int:
        return int((num_occurrences * (num_occurrences-1)) / 2)

    # Same logic applies, but we must also consider that if subarray summed to a modulo value 
    # of zero each of these ALSO needs be counted as a subarray divisible by k
    def get_zero_sub_count(self, num_occurrences: int) -> int:
        return int(((num_occurrences * (num_occurrences-1)) / 2) + num_occurrences)

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        running_sum = mod_value = 0 
        remaining_sum = defaultdict(int)                                            # Uninitialized keys -> map to a value of 0

        # Keep track of the running sum, map the modulo of
        # each sum to the amount of times we have encountered
        # that modulo value
        for num in A:
            running_sum += num
            mod_value = running_sum % K
            remaining_sum[mod_value] += 1
        
        output_count = 0
        for mod_val, num_occurrences in remaining_sum.items():
            if mod_val == 0:                                                        # Zero case includes each of the mod = 0 subarrays themselves
                output_count += self.get_zero_sub_count(num_occurrences)
            else:
                if num_occurrences > 1:                                             # There must be atleast 2 to have a middle subarray = K
                    output_count += self.get_sub_count(num_occurrences)
        
        return output_count



arr = [4,5,0,-2,-3,1]
s = Solution()
print(s.subarraysDivByK(arr, 5))