class Solution:
    def decodeString(self, s: str) -> str:
        # Edge cases
        if(not s):
            return ""
        if(len(s) == 1):
            return s
        
        st = []
        for char in s:                
            if(char == ']'):                            # End of segment reached
                decodedChars = []
                poppedChar = st.pop()
                while(poppedChar != '['):               # Build a reversed list of the segment's chars
                    decodedChars.append(poppedChar)
                    poppedChar = st.pop()
                
                # Quantity directly precedes opening bracket '['
                qty = []
                while(st and st[-1].isdigit()):
                    qty.append(st.pop())
                qty = int("".join(qty[::-1]))
                
                # Iterate backwards adding each char in the segment, qty amount of times
                for _ in range(int(qty)):           
                    for i in range(len(decodedChars)-1, -1, -1):
                        st.append(decodedChars[i])    
                        
            else:
                st.append(char)
                
        # Return the fully decoded string
        return "".join(st) 
            
            