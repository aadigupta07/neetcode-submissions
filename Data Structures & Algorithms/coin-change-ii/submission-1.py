class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # likely determining how many combinations to get to each value between 1 and amount
        # if you have the number of ways to get to 
        if amount == 0:
            return 1

        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        
        for j in range(len(coins) + 1):
            dp[0][j] = 1
        

        # how many combinations of amount i with j coins
        # dp[i-1][j] means using this coin, summing to amount 1 less
        # dp[i][j-1] means using this amount, summing without this coin
        # so relevantly we will need to check dp[i-coin][j] + dp[i][j-1]

        for i in range(1, amount+1):
            for j in range(1, len(coins) + 1):
                if i - coins[j-1] >= 0:
                    dp[i][j] += dp[i-coins[j-1]][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

        return dp[-1][-1]

