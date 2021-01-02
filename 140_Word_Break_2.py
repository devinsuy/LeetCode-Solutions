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
                return cache[end_index]
        
        return wordBreak_util(len(s))


'''
Output:
[
  "cats and dog",
  "cat sand dog"
]
'''
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]


'''
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
'''
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]


'''
Output:
[]
'''
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

s = Solution()
print(s.wordBreak(s, wordDict))