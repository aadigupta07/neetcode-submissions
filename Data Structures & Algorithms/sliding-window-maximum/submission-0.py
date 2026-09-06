from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices, values decreasing front->back
        result = []

        for r in range(len(nums)):
            # 1. Remove indices whose values are smaller than nums[r]
            #    (they can never be the max again)
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()

            # 2. Add current index
            dq.append(r)

            # 3. Remove front index if it's outside the window
            if dq[0] <= r - k:
                dq.popleft()

            # 4. Once window is full size, record the max
            if r >= k - 1:
                result.append(nums[dq[0]])

        return result