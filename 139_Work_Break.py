from typing import List 
from collections import defaultdict

class Solution:
    def in_str(self, s, word, indices):
        print("Checking", word, indices)
        # Check each potential index where the first
        # letter of the word matches
        for index in indices:
            end_index = index + len(word)
            word_index = 0
            for s_index in range(index, end_index):
                if s[s_index] != word[word_index]:
                    continue
                # print(s[s_index], word[word_index])
                # print(s_index, word_index)
                # print()
                word_index += 1
        
        return True


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Base cases


        indices = defaultdict(list)
        for i, letter in enumerate(s): indices[letter].append(i)
        
        for word in wordDict:
            if not self.in_str(s, word, indices[word[0]]):
                print(word, " not in")
                return False

        return True 
        
        
        
        

# Expected: True
s = "leetcode"
wordDict = ["leet", "code"]

# Expected: True
s = "applepenapple"
wordDict = ["apple", "pen"]


# Expected: True  
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]



sol = Solution()
print(sol.wordBreak(s, wordDict))