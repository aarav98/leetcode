class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        tab1 = {}
        for i in nums1:
            tab1[i] = tab1.get(i,0) + 1
        
        tab2 = {}
        for i in nums2:
            tab2[i] = tab2.get(i,0) + 1
            
        result = []
        for key, val in tab1.items():
            count = min(tab2.get(key,0), val)
            for i in range(count):
                result.append(key)
        
        return result
                
                
        