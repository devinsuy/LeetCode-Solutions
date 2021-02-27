class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Edge cases
        if(len(s) == 0):
            return True
        if(not wordDict):
            return False
        
        cache = [None] * len(s)
        def canSegment(i: int):
            # Base case
            if(i == len(s)):
                return True
            
            # Lookup result
            if(cache[i] is not None):
                return cache[i]
            
            # Recursively segment the characters, trying each word 
            # in wordDict at this pass
            for word in wordDict:
                nextIndex = i + len(word)
                if(nextIndex <= len(s) and s[i:nextIndex] == word and canSegment(nextIndex)):
                    cache[i] = True
                    return True
            
            # Was unable to segment the remaining indices using wordDict
            cache[i] = False
            return False
        
        return canSegment(0)
        