class Solution {
    private HashMap<Integer,Integer> cache;
    
    public int coinChangeUtil(int[] coins, int amount, int accumulator){
        if(this.cache.containsKey(amount))  // Lookup previous result
            return this.cache.get(amount);
        if(amount < 0)                      // Failed to make change
            return -1;
        if(amount == 0)                     // Change successfully made
            return accumulator;

        int minCoins = Integer.MAX_VALUE;
        int numCoins, nextAmount, subResult;
        
        // Iterate through each denomination and branch subproblems
        // the minimum for the current amount is the min of each of these
        for(int coin : coins){
            // Only branch if the next amount is valid
            subResult = coinChangeUtil(coins, amount-coin, accumulator+1);
            if(subResult != -1){
                numCoins = subResult + 1;
                if(numCoins < minCoins) minCoins = numCoins;
            }
        }
        
        if(minCoins == Integer.MAX_VALUE) minCoins = -1;
        this.cache.put(amount, minCoins);
        return minCoins;
    }
    
    public int coinChange(int[] coins, int amount) {
        // Intialize cache, amounts = a coin value only require 1 coin
        this.cache = new HashMap<>();
        for(int coin : coins) this.cache.put(coin, 1);
        
        return coinChangeUtil(coins, amount, 0);
    }
}