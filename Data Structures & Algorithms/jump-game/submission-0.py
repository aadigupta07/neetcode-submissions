class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        index = 0
        reach = nums[index]
        while index < len(nums)-1:
            if nums[index] == 0: # can't go further
                return False
            if index + reach >= len(nums)-1: # made it
                return True

            curr = index # check that you didn't find anything better
            # find next best option for reaching further out
            for i in range(index+1, index+reach+1): 
                if i + nums[i] > index + reach:
                    index = i
                    reach = nums[i]

            if index == curr:
                return False
        
        return True