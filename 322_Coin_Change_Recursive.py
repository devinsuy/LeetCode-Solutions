class Solution:
    def coinChange(self, coins, amount):
        # Memoization, map each amount to its min amount of coins
        cache = {0 : 0}
        for coin_val in coins: cache[coin_val] = 1
        
        # Recursive utility function
        def coinChange_util(curr_amount: int):
            if curr_amount in cache: 
                return cache[curr_amount]
            else:
                curr_min_coins = float('inf')
                # Branch on coin values to find minimum number
                for coin_val in coins:
                    next_amt = curr_amount - coin_val
                    if next_amt < 0: 
                        continue

                    next_coin_coint = coinChange_util(next_amt)
                    if next_coin_coint != -1:
                        curr_min_coins = min(curr_min_coins, next_coin_coint + 1)

                # Cache results, return minimum coins for amount if found
                if curr_min_coins == float('inf'): 
                    curr_min_coins = -1
                cache[curr_amount] = curr_min_coins 
                return curr_min_coins

        return coinChange_util(amount)


# Expected: 3
coins = [1,2,5]
amount = 11 

# Expected: -1
# coins = [2]
# amount = 3 

# Expected: 2
# coins = [1]
# amount = 2

# Expected: -1
# coins = [2]
# amount = 1

s = Solution()
print(s.coinChange(coins, amount))