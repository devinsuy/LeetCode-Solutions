from collections import defaultdict
from typing import List

class Partition:
    def __init__(self, index_range):
        self.min_index = index_range[0]
        self.max_index = index_range[1]

        # Maintain a set of numbers that still need to be allocated
        # before the partition can be complete
        self.remaining = set([]) 
        for i in range(self.min_index+1, self.max_index):
            self.remaining.add(i)
    
    def is_done(self):
        return len(self.remaining) == 0
    
    # Return the size of the partition
    def get_size(self):
        return self.max_index - self.min_index + 1 

    def remove(self, nums):
        self.remaining.difference_update(nums)

    # Check if a range is within the allotted partition, if
    # below or above, extend the partition window and update set
    def validate_range(self, index_range):
        low, high = index_range
        
        if low < self.min_index:
            for i in range(low+1, self.min_index):
                self.remaining.add(i)
            self.min_index = low

        if high > self.max_index:
            for i in range(self.max_index+1, high):
                self.remaining.add(i)
            self.max_index = high


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # Base cases
        if len(S) == 0: return [0]
        elif len(S) == 1: return [1]

        # Build mapping of letters to list of indices  
        letter_indices = defaultdict(list)
        for i, letter in enumerate(S): letter_indices[letter].append(i)
        
        # Map letters to the range of indicies they appear
        letter_range = {}
        for letter in S:
            curr_indices = letter_indices[letter]
            # The letter only appears once, its min and max index are the same 
            if len(curr_indices) == 1: 
                letter_range[letter] = (curr_indices[0], curr_indices[0])
            # Otherwise store the first and last index the letter appears at
            else:
                letter_range[letter] = (curr_indices[0], curr_indices[-1])
        
        last_finished = -1
        partition_sizes = []
        partitions = []
        while last_finished != len(S)-1:
            # Initialize the next partition
            next_letter = S[last_finished+1]
            curr_partition = Partition(letter_range[next_letter])
            curr_partition.remove(letter_indices[next_letter])

            while not curr_partition.is_done():
                letter = S[curr_partition.remaining.pop()] 
                curr_partition.validate_range(letter_range[letter])
                curr_partition.remove(letter_indices[letter])

            partition_sizes.append(curr_partition.get_size())
            last_finished = curr_partition.max_index
            partitions.append(curr_partition)

        return partition_sizes



# Expected: [9,7,8]
S = "ababcbacadefegdehijhklij"

s = Solution()
print(s.partitionLabels(S))