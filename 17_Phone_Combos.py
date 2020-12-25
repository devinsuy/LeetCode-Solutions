from typing import List
from copy import deepcopy 

class Solution:
    # Recursively generate combinations
    def letterCombinations_util(self, curr_str: str, digit_index: int):
        # Base case end of tree reached, save finished combination 
        if digit_index == self.exit_len:
            self.combos.append(curr_str)
            return

        curr_digit = self.digits[digit_index]
        
        # Branch next combinations on each possible letter for this digit
        for next_letter in self.num_letters[curr_digit]:
            next_str = deepcopy(curr_str) + next_letter
            self.letterCombinations_util(next_str, digit_index+1)


    def letterCombinations(self, digits: str) -> List[str]:
        # Map each digit to its corresponding set of letters
        # input is restricted to string of digits 2-9 inclusive
        self.num_letters = {
            '2' : ['a','b','c'], '3' : ['d','e','f'], '4': ['g','h','i'], '5' : ['j','k','l'],
            '6' : ['m','n','o'], '7' : ['p','q','r','s'], '8' : ['t','u','v'], '9' : ['w','x','y','z']
        }

        # Base case inputs
        if len(digits) == 0: return []
        elif len(digits) == 1 : return self.num_letters[digits]

        # Otherwise use recursive backtracking to generate all combinations
        self.combos = []
        self.digits = digits
        self.exit_len = len(digits)
        self.letterCombinations_util(curr_str="", digit_index=0)

        return self.combos





s = Solution()

# Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
digits = "23"

# Expected: ["a","b","c"]
# digits = "2"


print(s.letterCombinations(digits))