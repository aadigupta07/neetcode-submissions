class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = 0
        end = 1
        while end < len(prices) and start < len(prices)-1:
            curr = prices[end] - prices[start]
            profit = max(profit, curr)

            if end == len(prices)-1:
                start+=1
            elif end == start + 1 or prices[end+1] > prices[end]:
                end+=1
            else:
                start+=1
        
        return profit
