class Solution {
    private HashMap<Integer,Integer> cache;
    
    public int climbStairsUtil(int n){
        if(this.cache.containsKey(n))
            return this.cache.get(n);
        int numWays = climbStairsUtil(n-2) + climbStairsUtil(n-1);
        cache.put(n, numWays);
        
        return numWays;
    }
    
    public int climbStairs(int n) {
        // Initialize cache with base cases
        this.cache = new HashMap<>();
        this.cache.put(1, 1);
        this.cache.put(2, 2);
        
        return climbStairsUtil(n);
    }
}