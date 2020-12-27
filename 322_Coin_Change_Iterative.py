class Solution:
    def coinChange(self, coins, amount):
        # Base cases 
        if amount == 0: 
            return 0
        if amount in coins:
            return 1
        
        # Initialize base memo values, each coin value
        # from our coins can be reached in 1 coin
        self.cache = [None] * (amount+1)
        self.cache[0] = 0
        for coin in coins: 
            if coin < amount:
                self.cache[coin] = 1

        # Using bottom up approach, solve subproblems from 1:n
        for i in range(1, len(self.cache)):
            if not self.cache[i]:
                min_coins = float('inf')

                # If the subproblem subtracted by each coin value yields a previous
                # sub problem, solution is previous problem + the additional 1 coin
                for coin in coins:
                    if i-coin > 0 and self.cache[i-coin] < min_coins:
                        min_coins = self.cache[i-coin] + 1

                # Cache the minimum of each of these solutions
                self.cache[i] = min_coins
        
        # Return result if found
        output = self.cache[amount]
        if output == float('inf'): 
            return -1
        else: 
            return output