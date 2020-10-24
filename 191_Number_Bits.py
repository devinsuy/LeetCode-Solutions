# Input: Given an unsigned (positive) int
# Output: The number of 1 bits used to represent the int

# Assumptions:
#   An int will take up to n bits to represent where 2^n >= int
#   bin() function can be used to convert a number to a bit string

# Test Cases:
#   None or int < 0 -> None
#   0 -> 0
#   1 -> 1
#   2 -> 1
#   3 -> 2
#   4 -> 1
#   10 -> 2
#   11 -> 3

# Brute force O(n):
#   Convert the int to a binary string using bin() O(log n)
#   Perform a single pass through the string to count the number of "1" bits

# Alternate Solution O(n):
#   Use a top down greedy algorithm to count the number of "1" bits required to represent the number
#   Continue incrementing until we find the FIRST n value where 2^n >= 0
#       If 2^n == int : return 1
#   Increment bit count by one, subtract 2^n from our int, continue until the value reaches 0
#   Create a pow dictionary that maps n -> the value of 2^n, so we can lookup repeated exponent values in O(1)    
#   Rather than recompute it if this function will be called multiple times (at the cost of memory) which can become non negligible
#   for large values of n

exponent = {} # Maps exponent value n -> to the value 2^n

class Solution:    
    def two_pow(self, n):
        # Lookup the value O(1)
        if n in exponent:
            return exponent[n]
        
        # Calculate the value for the first time and store it 
        exponent_value = 2 ** n         # Can be manually implemnted with loop and multiplying by 2
        exponent[n] = exponent_value

        return exponent_value

    def hammingWeight(self, n: int) -> int:
        # Base cases
        if n is None or n < 0:
            return None

        num_bits = 0
        remaining_value = n

        # Count the number of bits required
        while remaining_value > 0:
            n = 0
            while self.two_pow(n) <= remaining_value:      # Locate the largest n value that satisfies 2^n < remaining_value
                n += 1

            # Bookkeeping
            remaining_value -= self.two_pow(n-1) 
            num_bits += 1
        
        return num_bits


s = Solution()
print(s.hammingWeight(11))