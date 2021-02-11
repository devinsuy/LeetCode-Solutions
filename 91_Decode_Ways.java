class Solution {
    HashMap<Integer, Integer> cache = new HashMap<>();
    public int numDecodings(String s) {
        return numDecodingsUtil(0, s);
    }
    
    public boolean isValid(int i, int j, String s){
        if(i >= s.length()){
            return false;
        }
        String sub = s.substring(i, j);
        if(sub.charAt(0) == '0'){
            return false;
        }
        int val = Integer.valueOf(sub);
        return val > 0 && val < 27;
    }
    
    private int numDecodingsUtil(int index, String s) {
        // Lookup previous result
        if(this.cache.containsKey(index)){
            return this.cache.get(index);
        }
        // End of string reached
        if(index == s.length()){
            return 1;
        }
        // Base case, decoding is valid if this last character is valid
        if(index == s.length() - 1){
            return this.isValid(index, index+1, s) ? 1 : 0;
        }
        
        int decodings = 0;
        if(this.isValid(index, index+1, s)){
            decodings += this.numDecodingsUtil(index+1, s);
        }
        if(this.isValid(index, index+2, s)){
            decodings += this.numDecodingsUtil(index+2, s);
        }
        this.cache.put(index, decodings);
        
        return decodings;
    }
        
}