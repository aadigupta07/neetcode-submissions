class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # track the max increasing subsequence up to each index
        # can loop through indexes before and update max if nums[i] > nums[prev_index]


        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


        