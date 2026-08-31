class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] +=1
        
        arr = []
        for n, count in freq.items():
            arr.append([count, n])
        
        arr.sort()
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
