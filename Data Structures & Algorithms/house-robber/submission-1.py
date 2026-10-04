class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums[0]
        if len(nums) == 1:
            return max(nums[0], num[1])
        # 2,1,1,2
        # any given number, three options
        # add to the max from 2 ago
        # skip since last one was already added
        # skip a second time in a row
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[len(nums)-1]