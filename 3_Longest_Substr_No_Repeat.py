# O(N^2)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0: return 0
#         elif len(s) == 1 : return 1
        
#         max_len = 1
#         for i in range(len(s)):
#             start_letter = s[i]
#             prev_letters = set([start_letter])
#             curr_len = 1
#             for j in range(i+1, len(s)):
#                 curr_len += 1 
#                 # Sliding window, only need to consider newly added letter
#                 if s[j] not in prev_letters:
#                     prev_letters.add(s[j])
#                     if curr_len > max_len:
#                         max_len = curr_len
#                 # Substring is not distinct, all following substrings starting
#                 # at this index will not be either, move on to next
#                 else:
#                     break

#         return max_len

# O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base cases
        if len(s) == 0: return 0
        elif len(s) == 1 : return 1
        
        # Maintain a running set of current letters
        max_len = curr_len = 1
        start_index = 0
        prev_letters = set([s[0]])

        # Sliding window, add to the running subtring one letter at a time       
        for i in range(start_index+1, len(s)):
            if s[i] not in prev_letters:
                prev_letters.add(s[i])
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
            # Added letter makes substring no longer distinct
            else:
                # Move starting position until we can add the current letter
                while s[i] in prev_letters:
                    prev_letters.remove(s[start_index])
                    start_index += 1
                prev_letters.add(s[i])
                curr_len = i - start_index + 1

        return max_len






s = Solution()
a = "abcabcbb"
b = "pwwkew"
c = "bbbbb"

print(s.lengthOfLongestSubstring(a))
