class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        
        counts = defaultdict(int)
        for i in prefix: # i tracks sum so far
            if i == k:
                total += 1
            if (i-k) in counts:
                total += counts[i-k]
            counts[i] +=1
        return total
