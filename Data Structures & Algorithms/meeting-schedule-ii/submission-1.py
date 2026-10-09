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

        rooms = 0
        most = 0
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        s, e = 0, 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                s+=1
                rooms+=1
            else:
                e+=1
                rooms-=1
            most = max(most, rooms)
        
        return most





        