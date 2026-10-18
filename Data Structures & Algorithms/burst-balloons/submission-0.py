class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        # length of interval
        for length in range(1, n - 1):
            for i in range(1, n - length):
                j = i + length - 1

                maximum = 0

                # try each balloon as the last one burst
                for a in range(i, j + 1):
                    coins = nums[i-1] * nums[a] * nums[j+1]
                    coins += dp[i][a-1] + dp[a+1][j]

                    maximum = max(maximum, coins)

                dp[i][j] = maximum

        return dp[1][n-2]