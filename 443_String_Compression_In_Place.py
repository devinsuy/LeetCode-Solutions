class Solution:
    def compress(self, chars: List[str]) -> int:
        # Edge cases
        if(len(chars) <= 1):
            return len(chars)
        
        prev = chars[0]
        qty = 1
        outPtr = 1
        
        # Build compressed string in space O(1) memory
        for i in range(1, len(chars)):
            curr = chars[i]
            if(curr == prev):
                qty += 1
            else:
                if(qty != 1):                           # Append quantity digit by digit and reset
                    qty = str(qty)
                    for i in range(len(qty)): 
                        chars[outPtr] = qty[i]
                        outPtr += 1
                    qty = 1
                    
                chars[outPtr] = curr
                outPtr += 1
                prev = curr
                
        # Add last quantity
        if(qty != 1):
            qty = str(qty)
            for i in range(len(qty)): 
                chars[outPtr] = qty[i]
                outPtr += 1
        
        # Remove any characters past the end of the compressed string
        for _ in range(len(chars) - outPtr):
            chars.pop()
        
        return len(chars)