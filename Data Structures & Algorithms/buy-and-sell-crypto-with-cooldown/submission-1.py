class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # any given day, if you sold the day before, you cannot buy
        # this means we likely need to track if we sold the day before, or if we are holding a neetcoin, 
        # Would immediately pick up the first neetcoin, I assume we would update the value of the neetcoin to a smaller one if we come across it
        # If you reach a higher number, you can either take the profit in one scenario, or hold on for a bigger number


        # state 0 is holding a coin
        # state 1 is empty
        # state 2 is just sold
        dp = [[0] * (len(prices) + 1) for _ in range(3)]
        
        # holding day one means you bought
        dp[0][0] -= prices[0]
        
        # holding is the max of holding, and empty - today's coin
        # empty is max of empty and cooldown from yesterday
        # just sold is holding + price today

        for i in range(1, len(prices) + 1):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] - prices[i-1])
            dp[1][i] = max(dp[1][i-1], dp[2][i-1])
            dp[2][i] = dp[0][i-1] + prices[i-1]
        
        return max( dp[1][len(prices)], dp[2][len(prices)])
