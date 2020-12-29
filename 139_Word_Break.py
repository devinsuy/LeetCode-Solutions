from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Lowercase all characters and remove whitespace
        words = set([word.lower() for word in wordDict])
        s = s.lower()
        s.replace(' ', '')

        # Map substrings to boolean (whether or not can break)
        cache = {'' : True}
        
        def wordBreak_util(substr: str):
            # Lookup result if subproblem solved before
            if substr in cache:
                return cache[substr]
                
            # Base case, was able to break into word
            if substr in words:
                cache[substr] = True
                return True
            
            # Substr cannot be further divided and is not a valid word
            if len(substr) == 1:
                return False
            
            left = 0
            right = len(substr) -1
            for right in range(len(substr)-1, -1, -1):
                curr_substr = substr[left:right]

                # Base case, cannot be further subdivided, only
                # breakable if substring in word set itelf 
                # if curr_substr == substr:
                #     breakable = substr in words
                #     cache[substr] = breakable
                #     return breakable

                # Recurse to find subdivisions of our substring
                curr_breakable = wordBreak_util(curr_substr)
                cache[curr_substr] = curr_breakable

                # Subproblem solved
                if curr_breakable:
                    break
            
            # A subproblem was solved, move on to subsequent subproblem
            breakable = wordBreak_util(substr[right:])
            cache[substr] = breakable

            return breakable

        return wordBreak_util(s)

# Expected: False
s = "catsandog"
words = ["cats", "dog", "sand", "and", "cat"]

# Expected: True 
s = "applepenapple"
words = ["apple", "pen"]

# Expected: True
#s = "leetcode"
#words = ["leet", "code"]

# Expected: True
#s = "aaaaaaa"
#words = ["aaaa","aaa"]

# Expected: True
#s = "goalspecial"
#words = ["go","goal","goals","special"]

sol = Solution()
print(sol.wordBreak(s, words))

print(list(range(1,len('leetcode')+1)))