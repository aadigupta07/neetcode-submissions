class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        lowest = prices[0]

        for i in range(1, len(prices)):
            curr = prices[i] - lowest
            profit = max(curr, profit)
            lowest = min(lowest, prices[i])
        
        return profit
            
