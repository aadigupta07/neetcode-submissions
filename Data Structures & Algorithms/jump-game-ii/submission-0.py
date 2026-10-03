class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        index = 0
        while index < len(nums)-1:
            if index + nums[index] >= len(nums)-1:
                return jumps+1  
            # can u reach? end check
            for i in range(index + 1, index + nums[index] + 1):
                if i + nums[i] > index + nums[index]:
                    index = i
            jumps+=1

        return jumps