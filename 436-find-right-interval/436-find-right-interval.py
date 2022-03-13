from heapq import heappush, heappop
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        max_start_heap = []
        max_end_heap = []
        
        result = [0 for i in range(n)]
        
        for i, interval in enumerate(intervals):
            heappush(max_start_heap, (-interval[0], i))
            heappush(max_end_heap, (-interval[1], i))
        
        for _ in range(n):
            top_end, top_end_i = heappop(max_end_heap)
            result[top_end_i] = -1
            
            if -max_start_heap[0][0] >= -top_end:
                top_start, top_start_i = heappop(max_start_heap)
                while max_start_heap and -max_start_heap[0][0] >= -top_end:
                    top_start, top_start_i = heappop(max_start_heap)
                result[top_end_i] = top_start_i

                heappush(max_start_heap, (top_start, top_start_i))
        return result
        
        