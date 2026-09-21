class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = [0] * len(nums)
        remainders = Counter()
        remainders[0] = 1

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        
        for i in range(0, len(nums)):
            curr = prefix[i] % k
            count += remainders[curr]
            remainders[curr] +=1
        return count
