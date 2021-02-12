class Solution {
    public int maxProfit(int[] prices) {
        // Base case
        if(prices.length == 0) return 0;
        
        int maxProfit = 0;
        int entryPrice = Integer.MAX_VALUE;
        int profit;
        
        for(int currPrice : prices){
            // Take a lower entry price if found
            entryPrice = (currPrice < entryPrice) ? currPrice : entryPrice;
            profit = currPrice - entryPrice;
            
            // Overwrite max profit if higher found
            maxProfit = (profit > maxProfit) ? profit : maxProfit;
        }
        return maxProfit;
    }
}