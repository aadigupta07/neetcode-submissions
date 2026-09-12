class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                break
        
        x = 0
        while True:
            if nums[x] == nums[slow]:
                return nums[slow]
            x = nums[x]
            slow = nums[slow]

        return 0