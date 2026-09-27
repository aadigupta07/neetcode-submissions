class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                if nums[r] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid-1
            else:
                if nums[r] > nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1