class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        seen = set(nums)
        i = 1
        while i <= len(nums):
            if i not in seen:
                result.append(i)
            i+=1

        return result
