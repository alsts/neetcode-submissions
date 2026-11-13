class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]: # profitable
                profit = max(profit, prices[r] - prices[l])
            else: # new lowest price found
                l = r
            r += 1

        return profit
