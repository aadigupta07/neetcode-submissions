class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True
        # track if its possible to sum to each index

        for num in nums:
            if num <= target:
                dp[num] = True
        
        # possible to sum to each value each value only once
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        
 
        
        
        return dp[target]
            
        
        

        