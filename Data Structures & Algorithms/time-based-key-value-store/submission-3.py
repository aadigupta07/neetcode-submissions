class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp)) # list is sorted by default since set is guaranteed rising
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.hashmap[key]) - 1
        result = ""
        while l <= r:
            mid = (l+r)//2
            curr = self.hashmap[key][mid][1]

            if curr <= timestamp:
                result = self.hashmap[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return result

        
