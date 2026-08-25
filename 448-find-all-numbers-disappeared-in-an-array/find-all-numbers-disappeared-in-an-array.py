class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set1 = set(nums)
        num1 = []
        for i in range(1,len(nums)+1):
            if i not in set1:
                num1.append(i)
        return num1

