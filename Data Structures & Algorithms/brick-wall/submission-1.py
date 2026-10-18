class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = defaultdict(int)
        for w in wall:
            so_far = 0
            for i in range(len(w) - 1):
                so_far += w[i]
                count[so_far] += 1
        
        maximum = 0
        for value in count.values():
            maximum = max(maximum, value)
        
        return len(wall) - maximum


