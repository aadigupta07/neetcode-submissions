class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = min(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])
            dp[i][1] = max(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])
            maximum = max(maximum, dp[i][1])

        
        return maximum

