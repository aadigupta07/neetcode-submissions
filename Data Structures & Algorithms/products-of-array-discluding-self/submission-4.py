class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # as I go, multiply index of i by product of all numbers before
        # as I come back, multiply result of i by product of all numbers after
        multiplier = 1
        for i in range(1, n):
            multiplier *= nums[i-1]
            result[i] *= multiplier
        
        multiplier = 1
        for i in range(n-2, -1, -1):
            multiplier *= nums[i+1]
            result[i]*= multiplier
        
        return result
        