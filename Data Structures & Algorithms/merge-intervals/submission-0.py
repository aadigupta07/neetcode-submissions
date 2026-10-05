class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        result = []
        i = 0
        while i < len(intervals)-1:
            # non overlapping
            if intervals[i][1] < intervals[i+1][0]:
                result.append(intervals[i])
                i+=1
                continue
            else:
                # if completely covered
                start = intervals[i][0]
                end = intervals[i][1]
                furthest = 0
                while i < len(intervals) and intervals[i][0] <= end:
                    furthest = max(intervals[i][1], furthest)
                    i+=1
                result.append([start, furthest])
        
        if i == len(intervals)-1 and intervals[i][0] > intervals[i-1][1]:
            result.append(intervals[i])
            
        
        return result

            
            

