class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result = []


        for i in range(len(intervals)):
            if not result:
                result.append(intervals[i])
            elif intervals[i][0] < result[-1][1]: # overlaps
                # keep the smaller end
                if intervals[i][1] < result[-1][1]:
                    result.pop()
                    result.append(intervals[i])
            else:
                result.append(intervals[i])
        
        return len(intervals) - len(result)
                
            