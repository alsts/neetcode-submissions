class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l -> lowest_price
        profit = 0

        # max - min = profit
        while r < len(prices): 

            if prices[r] > prices[l]: # profitable
                profit = max(profit, prices[r] - prices[l])
            else: # new lowest
                l = r
                
            r += 1

        return profit