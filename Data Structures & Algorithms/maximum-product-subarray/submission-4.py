class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = best = nums[0]

        for n in nums[1::]:
            a, b = cur_max * n, cur_min * n
            cur_max = max(a, b, n)
            cur_min = min(a,b,n)
            best = max(best, cur_max)
        
        return best
