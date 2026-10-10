class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # always pick the task with most left unless its used within last n
        # need to find largest count outside of most recent n
        # can just count cycles, throwing in idles if there are none outside ofm ost recent n

        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0

        while heap or queue: 
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

            if heap:
                amount = heapq.heappop(heap)
                amount*= -1
                amount-=1

                if amount != 0:
                    queue.append((-amount, time + n + 1))

            
            
            time +=1
        return time
            
            

            



