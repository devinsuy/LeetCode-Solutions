class Solution:
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def reverseString(self, s) -> None:
        # Use two pointer approach
        front_ptr = 0
        back_ptr = len(s) - 1

        while front_ptr < back_ptr:
            self.swap(s, front_ptr, back_ptr)
            front_ptr += 1
            back_ptr -= 1
            
        return s
        
s = Solution()
s.reverseString(["a","b","c","d","e"])