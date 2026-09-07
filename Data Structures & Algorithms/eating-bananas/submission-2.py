class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = 0
        lowest = float('inf')
        for pile in piles:
            r = max(r, pile)
        
        while l <= r:
            mid = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid) # math.ceil

            if hours <= h: # hours == h doesn't guarantee lowest solution
                lowest = min(lowest, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return lowest

