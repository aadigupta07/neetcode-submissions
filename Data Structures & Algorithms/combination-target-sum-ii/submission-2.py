class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start, path, total):
            if total > target:
                return
            if total == target:
                result.append(path[:])
                return
            
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                total += nums[i]
                backtrack(i+1, path, total)
                total -= nums[i]
                path.pop()
        
        backtrack(0, [], 0)
        return result
                    