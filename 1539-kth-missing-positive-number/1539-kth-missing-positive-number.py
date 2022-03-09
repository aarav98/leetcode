"""
2,3,4,7,11

"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        prev = 0
        for curr in arr:
            missing_nums = curr - prev - 1
            if missing_nums < k:
                k -= missing_nums
                prev = curr
            else:
                break
            
        return prev+k
                