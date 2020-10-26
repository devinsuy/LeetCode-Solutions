class Solution:
    def longestPalindromeUtil(self, s, left, right):
        # Continue expanding outward on both ends while in bounds and still palindrome
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # Loop terminates after one left decrement and right increment
        # must offset length by 1 to get actual length
        palin_length = right - left - 1
        if palin_length > self.max_len:
            self.max_len = palin_length
            self.longest = s[left+1:right]

    def longestPalindrome(self, s):
        if len(s) == 0: return ""
        if len(s) == 1: return s
        self.max_len = 1
        self.longest = s[0]

        # Move left and right from each "center"
        for i in range(len(s)):
            # Expand outward from single letter (odd length palindromes)
            self.longestPalindromeUtil(s, i, i)

            # Expand outward from 2 letter center (even length palindromes)
            self.longestPalindromeUtil(s, i, i+1)
        
        return self.longest

# Expected: "aba"
s = "babad"
sol = Solution()
print(sol.longestPalindrome(s))