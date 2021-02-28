class Solution:
    def compress(self, chars: List[str]) -> int:
        # Edge cases
        if(len(chars) <= 1):
            return len(chars)
        
        prev = chars[0]
        qty = 1
        output = [prev]
        
        for i in range(1, len(chars)):
            curr = chars[i]
            if(curr == prev):
                qty += 1
            else:
                if(qty != 1):                           # Append quantity digit by digit and reset
                    qty = str(qty)
                    for i in range(len(qty)): 
                        output.append(qty[i])
                    qty = 1
                output.append(curr)
                prev = curr
                
        # Add last quantity
        if(qty != 1):
            qty = str(qty)
            for i in range(len(qty)): 
                output.append(qty[i])      
        
        # Copy compressed string into original list
        for i in range(min(len(chars), len(output))):
            chars[i] = output[i]
            
        if(len(chars) < len(output)):                   # Append remaining characters
            chars.extend(output[len(chars):])
        elif(len(chars) > len(output)):
            for _ in range(len(chars) - len(output)):   # Remove excess characters
                chars.pop()
        
        return len(chars)