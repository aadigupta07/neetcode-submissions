class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [float('inf')] * (amount+1)
        for c in coins:
            if c <= amount:
                dp[c] = 1

        for i in range(amount+1):
            for c in coins:
                if i-c < 0:
                    continue
                dp[i] = min(dp[i], dp[i-c] + 1)
        
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]
