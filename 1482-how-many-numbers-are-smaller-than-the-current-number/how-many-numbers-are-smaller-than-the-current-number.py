class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        nums2 = sorted(nums)
        for i in nums:
            ans.append(nums2.index(i))
        return ans 
        

                    
        