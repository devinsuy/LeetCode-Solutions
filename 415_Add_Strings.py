class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Edge cases
        if(not num1 and not num2): return ""
        if(not num1 and num2): return num2
        if(not num2 and num1): return num1
        
        leftPtr = len(num1) - 1
        rightPtr = len(num2) - 1
        output = []
        hasCarry = False
        carry = 0
        
        # Begin building sum from least significant digit to most
        while(leftPtr > -1 or rightPtr > -1):
            # Strings may differ in length
            if(leftPtr > -1):
                leftVal = int(num1[leftPtr])
                leftPtr -= 1
            else:
                leftVal = 0
            if(rightPtr > -1):
                rightVal = int(num2[rightPtr])
                rightPtr -= 1
            else:
                rightVal = 0
            
            currSum = leftVal + rightVal
            if(hasCarry): currSum += carry
            hasCarry = currSum >= 10
            currVal = currSum % 10
            carry = currSum // 10
            output.append(str(currVal))
        
        # The most significant digits of the string resulted in a carry
        if(hasCarry):
            output.append(str(carry))
        
        return "".join(reversed(output))