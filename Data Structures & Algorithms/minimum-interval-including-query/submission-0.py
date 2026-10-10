import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        # pair each query with its original position, then sort by query value
        sorted_queries = []
        for idx in range(len(queries)):
            sorted_queries.append([queries[idx], idx])
        sorted_queries.sort()

        result = [-1] * len(queries)
        heap = []
        i = 0

        for q, idx in sorted_queries:
            # add every interval that starts at or before q
            while i < len(intervals) and intervals[i][0] <= q:
                start = intervals[i][0]
                end = intervals[i][1]
                size = end - start + 1
                heapq.heappush(heap, [size, end])
                i += 1

            # remove intervals that end before q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # smallest remaining interval contains q
            if heap:
                result[idx] = heap[0][0]

        return result