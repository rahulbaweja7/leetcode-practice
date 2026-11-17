class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mp = {}

        for num in nums:
            mp[num] = mp.get(num, 0) + 1

            if mp[num] > 1:
                return True

        return False
        