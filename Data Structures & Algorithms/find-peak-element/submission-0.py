class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2

            if mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                l = mid + 1
            
            if mid == len(nums)-1:
                if nums[mid] > nums[mid-1]:
                    return mid
                r = mid - 1

            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            
            elif nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        
        return l

        

