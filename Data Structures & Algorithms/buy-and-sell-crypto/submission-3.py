class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        lowest = prices[0]

        for i in range(1, len(prices)):
            profit = max(prices[i] - lowest, profit) # just keeping track of minimum and taking profit
            lowest = min(lowest, prices[i])
        
        return profit
            
