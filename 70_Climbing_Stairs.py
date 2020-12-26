class Solution:
    # Use recursion with memoization to generate solution
    def climbStairs_util(self, n: int):
        # Exit conditions
        if n in self.cache: 
            return self.cache[n]
        if n-1 in self.cache and n-2 in self.cache:
            curr_num_ways = self.cache[n-1] + self.cache[n-2]
            self.cache[n] = curr_num_ways
            return curr_num_ways
        
        # Recurse
        if n-2 not in self.cache:
            self.climbStairs_util(n-2)
        if n-1 not in self.cache:
            self.climbStairs_util(n-1)
        
        # Compute and store result
        curr_num_ways = self.cache[n-1] + self.cache[n-2]   
        self.cache[n] = curr_num_ways
        return curr_num_ways


    def climbStairs(self, n: int) -> int:
        self.cache = {0 : 1, 1 : 1}
        return self.climbStairs_util(n)


        



# Expected: 3
n = 3

s = Solution()
print(s.climbStairs(n))