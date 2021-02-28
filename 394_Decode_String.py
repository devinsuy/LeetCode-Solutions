class Solution:
    def decodeString(self, s: str) -> str:
        # Edge cases
        if(not s):
            return ""
        if(len(s) == 1):
            return s
        
        # Parse the quantity substring at the current index until '['' open bracket
        def parseQty(i: int):
            digit = []
            currChar = s[i]
            while(currChar != '['):
                digit.append(currChar)
                i += 1
                currChar = s[i]
            
            return i+1, int(''.join(digit))
        
        # Beginning just past '[', parse the internal characters until ']' close bracket
        def parseChars(i: int):            
            chars = []
            currChar = s[i]
            
            while(currChar != ']'):
                if(currChar.isdigit()):             # New segment found, parse this inner segment
                    i, decoding = parseSegment(i)
                    chars.extend(decoding)
                else:
                    chars.append(currChar)
                    i += 1
                currChar = s[i]
                    
            return i+1, chars
        
        # Determine the quantity and chars for the decoding, recursively called
        # if a digit is found while decoding the current segment
        def parseSegment(i: int):
            i, qty = parseQty(i)
            i, chars = parseChars(i)
            
            return i, chars * qty
        
        
        # Parse the string, decoding each time a digit is found
        i = 0
        output = []
        while(i < len(s)):
            currChar = s[i]
            if(currChar.isdigit()):                 # Start of a segment found, decode and extend
                i, decoding = parseSegment(i)
                output.extend(decoding)
            else:                                   # Otherwise append the character
                output.append(currChar)
                i += 1
        
        # Return the fully decoded string
        return "".join(output) 
            
            