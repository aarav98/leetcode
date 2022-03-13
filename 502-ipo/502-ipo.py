from heapq import heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
#         educative io

        min_capital_heap = []
        max_profit_heap = []
        
        for i, cap in enumerate(capital):
            heappush(min_capital_heap, (cap, i))
        
        available_capital = w
        
        for _ in range(k):
            while min_capital_heap and min_capital_heap[0][0] <= available_capital:
                cap, i = heappop(min_capital_heap)
                heappush(max_profit_heap, (-profits[i],i))
            
            if not max_profit_heap:
                break
            
            available_capital += -heappop(max_profit_heap)[0]
            
        return available_capital
        