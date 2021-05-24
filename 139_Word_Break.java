// Assumption: s and wordDict only contain lowercase alpha characters

import java.util.*;

class Solution {
    public boolean beginsWith(String s, String word){
        if(s.length() < word.length())
            return false;
        
        int left = 0;
        int right = word.length() - 1;
        while(left <= right){
            if(s.charAt(left) != word.charAt(left) || s.charAt(right) != word.charAt(right))
                return false;
            left++;
            right--;
        }
        return true;
    }
    
    public boolean wordBreak(String s, List<String> wordDict) {
        // BFS traversal
        Queue<String> q = new LinkedList<String>();
        q.add(s);
        HashSet<String> visited = new HashSet<String>();

        String curr, remaining;
        while(!q.isEmpty()){
            curr = q.poll();
            if(visited.contains(curr))
                continue;
            visited.add(curr);
            
            // Expand each pathway of selected words
            for(String word : wordDict){
                if(beginsWith(curr, word)){
                    remaining = curr.substring(word.length());
                    if(remaining.length() == 0){                    // End of string reached
                        return true;
                    }
                    q.add(remaining);
                }
                
            }
        }
        return false;
    }
}