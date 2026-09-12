class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums: # second solution, check other submission for fast/slow (tho this is lwk better)
            index = abs(num) - 1
            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1
        
        return -1
            
            