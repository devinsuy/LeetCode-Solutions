# Input: Array of prices for a stock where arr[i] is the price on day i
# Output: Maximum profit achievable given constraints

# Assumptions:
#   - Only allowed at most one transaction (one buy and one sell)
#   - We want to maximize profit
#   - You cannot sell a stock before buying it, buy comes before sell
#   - Profit = sell_price - buy_price
#   - In a decreasing list, profit is zero, we would never buy

# Test Cases:
#   [1] -> 0
#   [1,2] -> 1
#   [2,1] -> 0
#   [1,2,1] -> 1

#   [7,1,5,3,6,4] -> 5
#       - We would buy on the day price drops to 1
#       - We woul sell on day price rises to 6 (it is the highest price AFTER the buy point)
#   [7,6,4,3,1] -> 0
#       - Price continues to decrease, any buy would be sold for a loss
#   [1,2,3,4,5] -> 4
#       - Price increasing, enter day 0, hold until last day

# Psuedocode:

# For any day, we will NOT buy on that day if price is never a price to the right of it greater than price on that day
# Assume we determine viable buy days, max_profit is calculated with max(values to right of buy) - buy_price 
# Keep track of a max_value up until an index

# Brute force O(n^2):
# max_profit = 0
# for i (0 : end), find the max value in i+1 : end
# current_profit = max_value - arr[i]
# if current_profit > max_profit -> max_profit = current_profit
 
# Alternate O(nlogn), O(n) additional memory:
# Copy and sort values, largest is at arr[-1], second largest arr[-2] ...
# Maintain a largest_index that initially points to the last element in the list
# As we iterate forward in the array, maintain a seen values set
# If the value at our largest_index is in our seen_set, continue decrementing until we reach one that isnt
# This gives us the largest value to the RIGHT of our current value

# EX: [7,1,5,3,6,4]
#     [1,3,4,5,6,7] sorted
# First pass largest_index = 6
# But seen = [7], and arr[largest_index] = 7, decrement
# arr[i] = 7, largest value to right is arr[largest_index] = 6
# Then seen = [7,1] arr[i] = 1, largest is still 6
# ... continue until we get to seen = [7,1,5,3,6] and arr[i] = 6, arr[largest_index] = 6
# which is in our set, decrement, 5 is in our set, decrement, 4 is not in our set, continue ...

class Solution:
    # Given the seen set, sorted prices, current largest_ptr, and current_value
    # Return the index of the largest element > current_value not in the seen set
    # followed by whether a value was found
    def get_max_ptr(self, seen, max, largest_ptr, current_value):
        current_max = max[largest_ptr]
        if current_max not in seen:
            if current_max > current_value:
                return [largest_ptr, True]
            else: # There does not exist a value greater to the right of current_value 
                return [largest_ptr, False]
        
        while current_max in seen:
            largest_ptr -= 1
            current_max = max[largest_ptr]
            if current_max <= current_value:
                return [largest_ptr, False]
        
        return [largest_ptr, True]

    def maxProfit(self, prices):
        # Base Cases
        if prices is None or len(prices) == 1:
            return 0

        # Check if the prices are strictly decreasing over time O(n)
        price_increased = False
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                price_increased = True
                break 
        if not price_increased:                             # There is no viable buy
            return 0

        max = [x for x in prices]                           # Perform a deep copy of the prices O(n)
        max.sort()                                          # Sort the prices in ascending order O(nlogn)

        # Maintain a seen set which we can use for contains operation O(1)
        seen = set([])
        largest_ptr = len(prices) - 1
        max_profit = 0

        # Consider the max profit achievable for each day if we buy at that price
        for i in range(0, len(prices)-1):
            price = prices[i]
            seen.add(price)
            largest_ptr, value_found = self.get_max_ptr(seen, max, largest_ptr, price)
            print("At", price, "max ptr is", largest_ptr)

            # We have the index of the largest element to the right of our current one
            if value_found:
                max_price = max[largest_ptr]
                current_profit = max_price - price          # The maximum profit for a buy on this day
                if current_profit > max_profit:
                    max_profit = current_profit
        
        return max_profit
                



s = Solution()
print(s.maxProfit([2,1,2,0,1]))

[0,1,1,2,2]
