class Solution:
    def is_valid(self, s):
        if len(s) == 0 or s[0] == "0": return False 
        elif len(s) == 1: return True

        val = int(s)
        return val > 0 and val < 27

    def numDecodingsUtil(self, s, left, right):
        # Base case, passed end of string, not valid path
        if right >= len(s):
            return 0

        # Avoid reprocessing
        index_tuple = (left, right)
        if index_tuple in self.cache:
            return self.cache[index_tuple]

        if not self.is_valid(s[left:right+1]):
            return 0
        else:
            # End of string reached, valid decoding
            if right == len(s) - 1:
                return 1
        
        # Calculate decodings for single digit and two digits
        # for next decision pathway
        a = self.numDecodingsUtil(s, right+1, right+1)
        b = self.numDecodingsUtil(s, right+1, right+2)
        decodings = a + b
        self.cache[index_tuple] = decodings

        return decodings

    def numDecodings(self, s: str) -> int:
        # Maps index tuples (start, end) to its number of decodings
        self.cache = {}
        a = self.numDecodingsUtil(s, 0, 0)
        b = self.numDecodingsUtil(s, 0, 1)

        return a+b

# Expected: 1
s = Solution()
print(s.numDecodings("2101"))