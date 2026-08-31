class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        forward = [0] * length
        backward = [0] * length
        res = [0] * length
        forward[0] = nums[0]
        backward[length-1] = nums[length-1]
        for i in range (1, length):
            forward[i] = forward[i-1] * nums[i]
        
        for i in range(length-2,-1,-1):
            backward[i] = backward[i+1] * nums[i]

        for i in range(0, length):
            left = forward[i-1] if i > 0 else 1
            right = backward[i+1] if i < length-1 else 1
            res[i] = left * right
        
        return res