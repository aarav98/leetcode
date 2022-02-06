
"""

"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        lo, hi = 1, len(nums)-1
        
        while lo<=hi:
            mid = (lo+hi)//2
            count = sum(num <= mid for num in nums)
            
            if count > mid:
                dup = mid
                hi = mid-1
            else:
                lo = mid+1
        return dup
        