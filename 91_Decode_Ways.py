class Solution:
    def isValid(self, substr):
        if len(substr) == 0 or substr[0] == "0":
            return False
        val = int(substr)
        return val > 0 and val < 27
    
    def numDecodingsUtil(self, s, left, right):
        # Base case, end depth traversal
        if right >= len(s): 
            return 0
        
        # Avoid redudant checks        
        if (left, right) in self.cache:
            return self.cache[(left, right)]
        
        if not self.isValid(s[left:right+1]):
            return 0
        else:
            # End of string reached by decision tree
            if right == len(s) - 1:
                return 1        
  
        # Recurse next decision, sum single number chosen and 2 numbers chosen pathways
        num_decodings = self.numDecodingsUtil(s, right+1, right+1) + self.numDecodingsUtil(s, right+1, right+2)
        self.cache[(left, right)] = num_decodings
        
        return num_decodings
        
    
    def numDecodings(self, s: str) -> int:        
        # Map index tuple (start, end) indices -> to its # possible decodings
        self.cache = {}
        a = self.numDecodingsUtil(s, 0, 0)
        b = self.numDecodingsUtil(s, 0, 1)
        
        return a+b