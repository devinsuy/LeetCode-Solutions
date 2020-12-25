from typing import List 
from copy import deepcopy

class Solution:
    # Recursively generate all permutations
    def permute_util(self, curr_nums, num_index, remain_nums):
        # Base case, save permutation as tuple over list 
        # for performance and exit
        if num_index == self.exit_len:
            self.permutations.append(curr_nums)
        else:
            for next_num in remain_nums:
                # Branch on the next possible number and remove it from the 
                # remaining_nums set for the next recurse
                next_nums = deepcopy(curr_nums)
                next_nums.append(next_num)
                next_remain_nums = deepcopy(remain_nums)
                next_remain_nums.remove(next_num)
                self.permute_util(next_nums, num_index+1, next_remain_nums)

    def permute(self, nums: List[int]) -> List[List[int]]:        
        # Base input cases
        self.exit_len = len(nums)
        if self.exit_len == 0: return []
        elif self.exit_len == 1: return [nums]

        # Backtrack permutations
        self.permutations = []
        self.permute_util(curr_nums=[], num_index=0, remain_nums=nums)

        return self.permutations

s = Solution()

# Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
nums = [1,2,3]

# Expected: [[0,1], [1,0]]
#nums = [0,1]

# Expected: [[1]]
# nums = [1]

print(s.permute(nums))