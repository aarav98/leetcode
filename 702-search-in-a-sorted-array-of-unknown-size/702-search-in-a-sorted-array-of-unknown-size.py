# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 1
        while target > reader.get(right):
            left = right
            right <<= 1
            
        while left <= right:
            mid = left + ((right-left)>>1)
            
            num = reader.get(mid)
            
            if num == target:
                return mid
            
            if num > target:
                right = mid-1
            else:
                left = mid+1
            
        return -1
            