class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = [[]]
        
        for num in nums:
            new_subsets = []
            for subset in subsets:
                s = subset.copy()
                s.append(num)
                new_subsets.append(s)
            subsets += new_subsets
        return subsets