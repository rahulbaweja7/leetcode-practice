class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = {}

        for i, num in enumerate(nums):
            complement = target - num
        
            if complement in numbers:
                return [numbers[complement], i]
            
            numbers[num] = i

        return []