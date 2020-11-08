# Input: An unsigned integer
# Output: The unsigned integer that is represented by the reversed 32 bit string of the input

# Assumptions:
#   Many numbers can be represented in less than 32 bits and will likely need to be padded
#   with leading zeros to ensure the bit string is of length 32
#   From there we need to do a pass to flip each bit, then reconvert back to int and return it


class Solution:
    # # Given a string of 1s and 0s, "flip" each bit and return the new string
    # def reverse_bits_util(self, n):
    #     bit_arr = list(n)
    #     for i in range(len(n)):
    #         bit = bit_arr[i]
    #         if bit == "0":
    #             bit_arr[i] = "1"
    #         else:
    #             bit_arr[i] = "0"
        
    #     return "".join(bit_arr)
    
    # Given a bit string, return the reversed string

    def reverseBits(self, n: int) -> int:
        bit_str = str(bin(n))[2:]                   # Trim off leading '0b'
        num_leading_zeros = 32 - len(bit_str)
        bit_arr = [None] * 32

        # Add the leading zeros in
        for i in range(num_leading_zeros):
            bit_arr[i] = "0"
        
        # Add in our remaining bits
        for i in range(len(bit_str)):
            bit_arr[num_leading_zeros + i] = bit_str[i]
        
        # flipped_str = self.reverse_bits_util("".join(bit_arr))

        return int("".join(bit_arr)[::-1], 2)

        
        
            
s = Solution()
print(s.reverseBits(5))