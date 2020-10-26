class Solution:
    def longestPalindrome(self, s):
        self.maxlen = 0
        self.start = 0

        for i in range(len(s)):
            self.expandFromCenter(s,i,i)
            self.expandFromCenter(s,i,i+1)
            
        self.end = self.start + self.maxlen
        return s[self.start:self.end]


    def expandFromCenter(self,s,l,r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        substr_len = r - l - 1
        if self.maxlen < substr_len:
            self.maxlen = substr_len
            self.start = l + 1
