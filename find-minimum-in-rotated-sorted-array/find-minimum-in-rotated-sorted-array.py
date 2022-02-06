class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n==1 or nums[0]<nums[-1]:
            return nums[0]
        
        lo, hi = 0, n
        
        while lo < hi:
            mid = (hi+lo)//2
            
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            
            if nums[mid] > nums[0]:
                lo = mid+1
            else:
                hi = mid
        return lo
            
        