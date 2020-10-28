# Input: Set of coin values, target value
# Output: The minimum number of coins needed to sum to target value, else -1 if DNE

# Assumptions:
#   - We may be given a value that is not possible to sum to with our given coin set
#   - Greedy algorithm will NOT always yield the correct answer
#   - min_coins(i) = min_coins(i-c) + 1 where c is a coin in {c1, c2, c3}
#   - The optimal solution can be found recursively from its subcases
#   - We can use memoization to cache optimal values instead of recalculating them

# Proceedure:
#   - Check which coins would be valid to take, i.e. val - c is >=0 otherwise don't take it (return -1)
#   - "Decision tree" at each depth is if we took c1 vs taking c2 vs taking c3, increment coin count each time
#   - Base case, return when val == 0




class Solution:
    def __init__(self):
        self.cache = {}  # Maps val -> to the min number of coins to make val
    def coin_change_util(self, coins, amount: int) -> int:
        # Base case
        if amount == 0:
            return 0
        
        # Perform recursive calls for each coin decision
        subcoin_vals = {}                                               # Maps the coin decision at the depth to the min number of coins for it
        for coin in coins:
            print("Cache:", self.cache)
            sub_val = amount - coin
            print("Param amt:", amount, " coin:", coin, " subval:", sub_val, "\n")
            if sub_val < 0:                                             # Not possible to make change for this value on this decision path
                continue
                
            if sub_val in self.cache:                                   # Perform lookup of previously calculated value
                sub_num_coins = self.cache[sub_val]
            else:                                                       # Perform recursive call
                sub_num_coins = self.coin_change_util(coins, sub_val)
                self.cache[sub_val] = sub_num_coins                     # Cache value for later use 

            # We reached an unsolvable subproblem, rendering our current problem
            # unsolvable, not possible to make change for this value with given coins
            if sub_num_coins == -1:
                subcoin_vals[amount] = -1
            # Otherwise take the optimal count for the subproblem and "take" the coin for that decision path
            else:
                subcoin_vals[amount] = sub_num_coins + 1
        
        # We were unable to make change using any coin
        if len(subcoin_vals) == 0:
            self.cache[amount] = -1
            return -1
            
        
        print("For val", amount, "Subcoin vals:", subcoin_vals)
        print("Returning", min(subcoin_vals.values()),"\n")
        return min(subcoin_vals.values())
            
    
    def coinChange(self, coins, amount: int) -> int:
        if amount is None or coins is None or amount < 0:           # Validation cases
            return -1
        self.cache.clear()  # Reset cache after each function call (so can be called consecutively with different coin sets)
        print(coins)
        print(amount)
        
        # Recursively find optimal solutions
        a = self.coin_change_util(coins, amount)
        print("A: ", a)
        print(self.cache)
        return a
        

s = Solution()
print(s.coinChange([2,5,10,1], 27))