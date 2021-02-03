class Solution {
    public static boolean isPalindrome(String s) {
        // Empty string and single character are considered palindromes
        if(s.length() <= 1){
            return true;
        }
        
        // Preprocess string
        StringBuilder sClean = new StringBuilder();
        char c;
        for(int i = 0; i < s.length(); i++){
            c = s.charAt(i);
            if (Character.isLetterOrDigit(c)){
                sClean.append(Character.toLowerCase(c));
            }
        }
        
        // Use 2 pointers to check if palindrome
        int left = 0;
        int right = sClean.length()-1;
        while(left < right){
            if(sClean.charAt(left++) != sClean.charAt(right--)){
                return false;
            }
        }
        return true;
    }
}