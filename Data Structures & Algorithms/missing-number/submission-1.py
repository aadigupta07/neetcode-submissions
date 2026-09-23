class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n  # start by including the extra index n (loop below only goes to n-1)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result