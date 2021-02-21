from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # Edge case
        if(len(s) < minSize):
            return 0
        
        # Map substring to its # of occurrences
        substrCount = defaultdict(int)
        maxCount = 0
        
        for i in range(len(s)):
            # Substring of size greater than minSize will have a count <= that of those with minSize
            # since we are looking for max count only consider those of minSize
            #   EX: For 2 <= size <= 3, "aa" "aaa" are both valid but "aa" more likely to have higher count
            substr = s[i:i+minSize]
            
            if(len(substr) < minSize): 
                continue
            if(len(set(substr)) <= maxLetters):
                substrCount[substr] += 1
                if(substrCount[substr] > maxCount): maxCount = substrCount[substr]
                    
        return maxCount