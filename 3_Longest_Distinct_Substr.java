// Longest without repeating CHARACTERS
//      Characters can be: letters, digit, symbol, spaces
class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Base case
        if(s.length() < 2)
            return s.length();
        
        HashSet<Character> seen = new HashSet<>();
        seen.add(s.charAt(0));
        char leftChar, rightChar;
        int left, right, subLen, maxLen;
        left = 0;
        right = maxLen = 1;
        
        // Sliding window O(n), left window constricts when duplicate found
        // until duplicate removed from left side or left = right, then right 
        // continues until end of the string
        while(right < s.length()){
            rightChar = s.charAt(right);
            if(!seen.contains(rightChar)){
                seen.add(rightChar);
                subLen = right - left + 1;
                if(subLen > maxLen)
                    maxLen = subLen;
                right++;
            } 
            else {    
                // Substring is no longer fully distinct, move left pointer 
                // forward until the substring is distinct again
                while(seen.contains(rightChar)){
                    seen.remove(s.charAt(left));
                    left++;
                }
            }
        }
        return maxLen;
    }
}