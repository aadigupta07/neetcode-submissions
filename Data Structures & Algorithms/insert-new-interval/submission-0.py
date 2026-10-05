class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # goes before everything
        # goes after everything
        # goes in between cases
        # 1. new_start > start of some other interval and less than end
        # start is new start, go until you get an end beyond inserted end
        # 2. new_end > start of some other interval and less than end
        # start is original start, end is new end
        # 3. either fully enveloped or full envelops existing
        
        
        start, end = newInterval[0], newInterval[1]
        result = []
        if len(intervals) == 0: # empty list
            return [[start, end]]
        
        if intervals[len(intervals)-1][1] < start: # goes at the very end without overlap
            intervals.append([start, end])
            return intervals


        for i in range(len(intervals)):
            # it just gets inserted if its before the interval entirely
            if end < intervals[i][0]:
                result.append([start, end])
                return result + intervals[i:]
            
            # completely after
            elif start > intervals[i][1]:
                result.append(intervals[i])
            else:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])

        result.append([start, end])       
                
            
        
        return result
