# Input: A string of only characters (){}[]
# Output: True if the input string is valid, False otherwise
#   Valid if each that is opened is close, and when closed done so in the correct order

# Assumptions:
# Input will not contain any other characters
# Input will contain ATLEAST 1 character, and at most 10,000
# We can only close with the same type of character that opened

class Solution:
    # Given a symbol, return the matching symbol
    def get_matching_symbol(self, symbol):
        if symbol == "(":
            return ")"
        elif symbol == ")":
            return "("
        elif symbol == "{":
            return "}"
        elif symbol == "}":
            return "{"
        elif symbol == "[":
            return "]"
        elif symbol == "]":
            return "["
        else:
            return None 

    def isValid(self, s: str) -> bool:
        # Base Cases
        if s == None or len(s) == 1:
            return False

        open_symbols = set(["(", "{", "["])
        
        # Use a LIFO structure that contains opened symbols, we pop from it
        # if we get a corresponding closing symbol for the most recent open
        stack = []  

        for symbol in s:
            if symbol in open_symbols:
                stack.append(symbol)
            else:
                if not stack:           # We have received a close even though there are no current open symbols
                    return False 

                if self.get_matching_symbol(stack[-1]) == symbol:
                    stack.pop()                
                else:                   # A closing symbol should only be closing the most recently opened symbol
                    return False
        
        # True if each open was matched to a close properly (stack is empty)
        return not stack

        
s = Solution()
print(s.isValid("(])"))