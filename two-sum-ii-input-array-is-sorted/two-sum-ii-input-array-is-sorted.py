class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        front, last = 0, len(nums)-1
        while front < last:
            if nums[front] + nums[last] == target:
                return [front+1, last+1]
            elif nums[front] + nums[last] < target:
                front+=1
            else:
                last-=1

        