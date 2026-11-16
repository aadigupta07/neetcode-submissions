class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        
        i = 0
        while i < len(nums):
            current = []
            first = nums[i]

            for j in range(i, i+3):
                if nums[j] - first > k:
                    return []
                else:
                    current.append(nums[j])

            result.append(current[:])
            i+=3
        
        return result
