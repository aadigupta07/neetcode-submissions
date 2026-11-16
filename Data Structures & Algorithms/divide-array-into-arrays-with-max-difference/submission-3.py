class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        
        i = 0
        while i < len(nums):
            current = []
            first = nums[i]
            last = nums[i+2]

            if last-first > k:
                return []
            else:
                result.append(nums[i:i+3])
            i+=3
        
        return result
