class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        tab1 = {i:True for i in nums1}
        tab2 = {i: True for i in nums2}
        result = []
        for key, exist in tab1.items():
            if tab2.get(key, False):
                result.append(key) 
        
        return result