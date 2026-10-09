"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        intervals.sort(key = lambda x: x.start)
        meetings = 0

        i = 1
        
        while i < len(intervals):
            meetings+=1
            reached = False
            # completely enveloped
            while i < len(intervals) and intervals[i].start >= intervals[i-1].start and intervals[i].end <= intervals[i-1].end:
                reached = True
                i+=1
            if not reached:
                i+=1
            

        
        return meetings

        