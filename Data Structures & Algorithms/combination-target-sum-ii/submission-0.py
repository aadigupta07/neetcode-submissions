class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        completed = set()

        def backtrack(start, path, total):
            if total > target:
                return
            if total == target:
                if not tuple(path) in completed:
                    result.append(path[:])
                    completed.add(tuple(path))
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                total += nums[i]
                backtrack(i+1, path, total)
                total -= nums[i]
                path.pop()
        
        backtrack(0, [], 0)
        return result
                    