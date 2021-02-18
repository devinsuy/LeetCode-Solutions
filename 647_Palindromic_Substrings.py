class Solution:
    def countSubstrings(self, s: str) -> int:
        # Edge cases
        if(s == None): return 0
        if(len(s) < 2): return 1
        
        # Intitalize memo, new palindrome substrings build on previous ones
        dp = []
        for _ in range(len(s)): dp.append([None] * (len(s)+1))
        for i in range(len(s)): 
            dp[i][i] = True                     # All empty are palindromes
            dp[i][i+1] = True                   # All singletons are palindromes
      
        def isPalin(start: int, end: int) -> bool:     
            # Lookup previous result
            if(dp[start][end] != None):
                return dp[start][end]
            
            # The string is a palindrome if excluding the first and last characters
            # is a palindrome and the first and last characters are the same
            if(isPalin(start+1, end-1) and s[start] == s[end-1]):
                dp[start][end] = True
                return True
            
            # Use 2 pointer approach
            isPalindrome = True
            left = start
            right = end-1
            while(left < right):
                # Disregard spaces in palindrome checking
                if(s[left] == ' '): left += 1
                if(s[right] == ' '): right -= 1
                else:
                    # A palindrome should be identical forwards and back
                    if(s[left] != s[right]):
                        isPalindrome = False
                        break
                    left += 1
                    right -= 1
            dp[start][end] = isPalindrome
            
            return isPalindrome
        
        # Iterate through all substrings, checking if palindrome
        numPalins = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if(isPalin(i, j)): 
                    numPalins += 1
        
        return numPalins
            