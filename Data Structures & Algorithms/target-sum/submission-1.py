class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # per column to include first j numbers, 
        # per row to combos up to an amount

        dp = [[0] * (2*abs(target) + 1) for _ in range(len(nums) + 1)]

        # array is twice as long, with target being middle index
        # every column index - target is the real amount you are trying to get to

        # row is how many numbers, column is target
        dp[0][abs(target)] = 1

        # assuming initialization is solved, you can add dp[i-1][j - num] + dp[i-1][j+num]

        for i in range(1, len(nums) + 1):
            num = nums[i-1]
            for j in range((2*target + 1)):
                if j-target-num >= 0:
                    dp[i][j] += dp[i-1][j-target - num]
                if 0 <= j-target+num <= 2*target + 1:
                    dp[i][j] += dp[i-1][j-target + num]
        
        return dp[-1][-1]
                

        


