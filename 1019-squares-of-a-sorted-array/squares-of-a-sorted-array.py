class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        arr = []
        for i in nums:
            arr.append(i*i)
        arr = sorted(arr)
        return arr
        