class Solution:
    def decodeString(self, s: str) -> str:
        # Edge cases
        if(not s):
            return ""
        if(len(s) == 1):
            return s
        
        # Build output stack and quantity stack together
        st = []
        qtySt = []
        i = 0
        
        while(i < len(s)):
            char = s[i]
            
            # Parse the entire digit and push to qtySt
            if(char.isdigit()):
                digits = []
                while(char.isdigit()):
                    digits.append(char)
                    i += 1
                    char = s[i]
                qtySt.append(int("".join(digits)))
            
            # End of segment reached
            elif(char == ']'):                            
                decodedChars = []
                poppedChar = st.pop()
                while(poppedChar != '['):               # Build a reversed list of the segment's chars
                    decodedChars.append(poppedChar)
                    poppedChar = st.pop()
                
                # Iterate backwards adding each char in the segment, qty amount of times
                for _ in range(qtySt.pop()):           
                    for j in range(len(decodedChars)-1, -1, -1):
                        st.append(decodedChars[j])    
                i += 1
            
            # Regular character, continue pushing to output st until segment ends
            else:
                st.append(char)
                i += 1 
                
        # Return the fully decoded string
        return "".join(st) 
            
            