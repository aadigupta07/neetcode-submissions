class MedianFinder:
    # lower is max heap, storing negative
    # upper is min heap, storing positive

    # for adding numbers, keep list lengths as even as possible
    # if one stack is less, push to it
    # check if tops of each stack need to be swapped after
    # use negation for comparison, not abs, since num can be positive or negative

    def __init__(self):
        self.upper = []
        self.lower = []

    def addNum(self, num: int) -> None:
        if not self.upper and not self.lower: # default push to upper because why not
            heapq.heappush(self.upper, num)
            return
        
        # heap push
        if len(self.upper) == len(self.lower):
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num)

        # swap check
        if self.upper[0] < -self.lower[0]:
            upper_temp = heapq.heappop(self.upper)
            lower_temp = -heapq.heappop(self.lower)
            
            heapq.heappush(self.upper, lower_temp)
            heapq.heappush(self.lower, -upper_temp)
        

        

        
        


        

    def findMedian(self) -> float:
        if not self.upper and not self.lower:
            return 0
        elif not self.upper:
            return -self.lower[0]
        elif not self.lower:
            return self.upper[0]


        if len(self.upper) == len(self.lower):
            return (self.upper[0] + -self.lower[0])/2
        elif len(self.upper) > len(self.lower):
            return self.upper[0]
        else:
            return -self.lower[0]
        