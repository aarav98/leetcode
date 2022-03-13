class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = deque()
        permutations.append([])
        for num in nums:
            for _ in range(len(permutations)):
                permutation = permutations.popleft()
                for i in range(len(permutation)+1):
                    permutation_copy = permutation.copy()
                    permutation_copy.insert(i, num)
                    permutations.append(permutation_copy)
        
        return permutations
        