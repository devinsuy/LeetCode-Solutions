# Input: Two arrays of integers 
# Output: An array of the intersection of the two input arrays

# Assumptions
#   We cannot consider sets as duplicates will not be tracked
#       The output array must contain each element the amount of times they are intersected
#       EX: [0,0,0,1,2] and [0,0,3] would return [0,0]
#   The ordering of the output array DOES NOT matter

# Test cases:
#   None or disjoint arrays:
#       return []
#   [1,2,2,1] and [2,2]:
#       return [2,2]

# Obtain a count of each element, do this separately for both lists
#   Store this in a hash, where the integer -> maps to the number of times it occurs
# Take the set intersection of the keys, these are the numbers we want for our output arr
#   Iterate through the key,values for one of the lists, if we find a number with an occurrence number > 1
#   We have to check the occurrences in the other hash, take the min of these two and that will give us
#   the number of times to include this element in our output array

class Solution:
    def intersect(self, nums1, nums2):
        # Base Cases
        if nums1 is None or nums2 is None or len(nums1) == 0 or len(nums2) == 0:
            return []

        occurrences_one = {}
        occurrences_two = {}

        # We can easily iterate over our lists concurrently O(n)
        if len(nums1) == len(nums2):
            for i in range(len(nums1)):
                num_one = nums1[i]
                num_two = nums2[i]
                
                # Map the values to their occurrences
                if num_one not in occurrences_one:
                    occurrences_one[num_one] = 1
                elif num_one in occurrences_one:
                    occurrences_one[num_one] += 1
                
                if num_two not in occurrences_two:
                    occurrences_two[num_two] = 1
                elif num_two in occurrences_two:
                    occurrences_two[num_two] += 1
        else:
            stop_index = max([len(nums1), len(nums2)])

            for i in range(stop_index):
                if i < len(nums1):
                    num_one = nums1[i]
                    if num_one not in occurrences_one:
                        occurrences_one[num_one] = 1
                    elif num_one in occurrences_one:
                        occurrences_one[num_one] += 1
                if i < len(nums2):
                    num_two = nums2[i]
                    if num_two not in occurrences_two:
                        occurrences_two[num_two] = 1
                    elif num_two in occurrences_two:
                        occurrences_two[num_two] += 1

        duplicates = set(occurrences_one.keys()).intersection(set(occurrences_two.keys()))

        # The lists share no similar elements
        if len(duplicates) == 0:
            return []

        intersect_arr = []

        # Begin building output arr
        for key in duplicates:
            count_one = occurrences_one[key]
            if count_one > 1:
                min_count = min([count_one, occurrences_two[key]])
                for i in range(min_count):                              # We will append the key as many times as they occur in BOTH arrays
                    intersect_arr.append(key)
            else:
                intersect_arr.append(key)
        
        return intersect_arr

s = Solution()
print(s.intersect([1,2,4,4], [4,5]))

