class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def time_to_min(time: str) -> int:
            return int(time[0:2]) * 60 + int(time[3:5])
        
        timePoints.sort(key = lambda x: time_to_min(x))

        latest = time_to_min(timePoints[-1])
        day = 24 * 60
        minimum = day

        for i in range(0, len(timePoints)-1):
            time1 = time_to_min(timePoints[i])
            time2 = time_to_min(timePoints[i+1])
            if time1 == latest or time1 == time2:
                return 0
            difference = min(time2 - time1, day-(latest - time1))

            minimum = min(minimum, difference)
        
        return minimum

        
        


