from typing import List
from copy import deepcopy

class Solution:
    def generateParenthesis_util(self, curr_str, open_left, remain_left, remain_right):
        # Base case, end of tree reached
        if len(curr_str) == self.n * 2:
            self.output.append(curr_str)

        # Otherwise recurse:
        # Successor state will append "("
        if remain_left > 0:
            curr_str += "("
            self.generateParenthesis_util(curr_str, open_left+1, remain_left-1, remain_right)
            curr_str = curr_str[:-1]
        
        # Successor state will append ")", closing a 
        # previously open "("
        if open_left > 0 and remain_right > 0:
            curr_str += ")"
            self.generateParenthesis_util(curr_str, open_left-1, remain_left, remain_right-1)
            curr_str = curr_str[:-1]            
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.output = []
        self.n = n
        self.generateParenthesis_util("", 0, n, n)

        return self.output


s = Solution()



# Expected: ["()"]
n=1
# Expected: ["((()))","(()())","(())()","()(())","()()()"]
n=3

print(s.generateParenthesis(n))
