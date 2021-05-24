public class Solution {
    public static String longestPalindrome(String s) {
        // Edge case
        if(s.length() == 1)
            return s.substring(0);
        
        String longestPalin = "";
        int n = s.length();
        boolean[][] dp = new boolean[n+1][n+1];
        
        // Initialize all empty and 1 letter palindromes
        dp[n][n] = true;
        for(int i = 0; i < n; i++){
            dp[i][i] = dp[i][i+1] = true;
            longestPalin = s.substring(i, i+1);
        }
        
        // Initialize all 2 letter palindromes
        for(int i = 0; i < n-1; i++){
            dp[i][i+2] = s.charAt(i) == s.charAt(i+1);
            if(dp[i][i+2])
                longestPalin = s.substring(i, i+2);
        }
        
        // Bottom up approach to build remaining palindromes
        boolean sameStartEnd;
        String currSubstr;
        for(int i = n-1; i >= 0; i--){
            for(int j = i; j <= n; j++){
                if(j-i <= 2)
                    continue;
                // Longer substring is a palindrome if its first and last characters are the 
                // same & the string without the first and last characters is a palindrome
                sameStartEnd = s.charAt(i) == s.charAt(j-1);

                dp[i][j] = sameStartEnd && dp[i+1][j-1]; 
                
                // Track max length
                if(dp[i][j]){
                    currSubstr = s.substring(i, j);
                    if(currSubstr.length() > longestPalin.length())
                        longestPalin = currSubstr;
                }
            }
        }
        return longestPalin;
    }
}