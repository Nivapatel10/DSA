class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1 = []
        count=0
        for i in nums :
            for j in nums:
                if j!=i and j<i:
                    count+=1
            nums1.append(count)
            count=0
        return nums1
                    
        