class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        # track if its possible to sum to each index

        for num in nums:
            if num <= target:
                dp[num] = True
        
        # possible to sum to each value

        for i in range(target+1):
            for num in nums:
                if i - num < 0:
                    continue
                if dp[i-num]:
                    dp[i] = True
        
        return dp[target]
            
        
        

        