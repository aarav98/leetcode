from heapq import *

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        """
        1,4,2,7,1,2,3
        
        max = [-1,-1,-2]
        min = [7,4,2]
        """
        
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap,-num)
        else:
            heappush(self.min_heap,num)
        
        if len(self.max_heap)-1 > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
        
        

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2
        return -self.max_heap[0]
    


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()