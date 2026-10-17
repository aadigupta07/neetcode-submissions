class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        for i in range(1, n+1):
            self.heap.append(i)
        
        heapq.heapify(self.heap)


        
    def reserve(self) -> int:
        curr = heapq.heappop(self.heap)

        return curr

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
