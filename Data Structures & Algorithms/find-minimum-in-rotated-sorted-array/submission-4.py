class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1


        while l < r:
            mid = (l+r)//2
            
            if nums[mid] > nums[r]: # comparisons with mid to find the split
                l = mid + 1
            if nums[mid] <= nums[r]:
                r = mid
        
        return nums[l]