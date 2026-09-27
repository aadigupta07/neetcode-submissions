class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maximum = float('-inf')
        for num in nums:
            total = max(total+num, num)
            maximum = max(maximum, total)

        return maximum