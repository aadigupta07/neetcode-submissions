class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # per column to include first j numbers, 
        # per row to combos up to an amount
        target = abs(target)
        total = sum(nums)

        dp = [[0] * (2*total + 1) for _ in range(len(nums) + 1)]

        # array is twice as long, with target being middle index
        # every column index - target is the real amount you are trying to get to

        # row is how many numbers, column is target
        dp[0][total] = 1

        # you can add dp[i-1][j - num] + dp[i-1][j+num]

        for i in range(1, len(nums) + 1):
            num = nums[i-1]
            for j in range((2*total + 1)):
                if j-num >= 0:
                    dp[i][j] += dp[i-1][j-num]
                if j + num <= 2 * total:
                    dp[i][j] += dp[i-1][j+num]
                
        
        return dp[-1][total + target]
                

        


