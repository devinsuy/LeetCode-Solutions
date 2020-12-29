from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Lowercase all characters and remove whitespace
        s = s.lower()
        s.replace(' ', '')
        cache = [None] * (len(s) + 1)
        
        def wordBreak_util(end_index: int):
            # Base case, string was segmented
            if end_index == 0:
                return True
            
            # Solve subproblem
            if cache[end_index] is None:
                for word in wordDict:
                    word_len = len(word)
                    start_index = end_index - word_len
                    if s[start_index:end_index] == word and wordBreak_util(end_index-word_len):
                        cache[end_index] = True
                        return True

                cache[end_index] = False
            else:
                print("Cache hit")
                return cache[end_index]
        
        return wordBreak_util(len(s))



# Expected: False
s = "catsandog"
words = ["cats", "dog", "sand", "and", "cat"]

# Expected: True 
# s = "applepenapple"
# words = ["apple", "pen", "ple", "ap"]

# Expected: True
# s = "leetcode"
# words = ["leet", "code"]

# Expected: True
# s = "aaaaaaa"
# words = ["aaaa","aaa"]

# # # Expected: True
# s = "goalspecial"
# words = ["go","goal","goals","special"]

sol = Solution()
print(sol.wordBreak(s, words))

