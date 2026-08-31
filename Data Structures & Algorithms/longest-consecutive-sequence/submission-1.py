class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        checked = set()
        max = 0

        for n in nums:
            count = 1

            if n in checked:
                continue
            checked.add(n)

            while True:
                if n + 1 in seen:
                    checked.add(n+1)
                    count += 1
                    n +=1
                else:
                    break

            if count > max:
                max = count        
                

        return max